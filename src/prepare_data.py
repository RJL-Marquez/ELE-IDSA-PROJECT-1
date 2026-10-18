"""Build the analysis dataset for the Route 801 bus bunching project.

Steps: load -> filter -> convert types -> clean -> impute -> derive variables -> save.

Usage (from the repo root):
    python src/prepare_data.py                      # uses data/raw/route_801_direction_6_clean.zip
    python src/prepare_data.py --raw path/to/APC_Raw_July_2021_December_2021.csv
                                                    # starts from the full 3.7 GB raw file instead

Outputs (in data/processed/):
    route801_events.csv.gz   one row per bus per stop, cleaned and ready to plot
    stops.csv                stop IDs in route order
    cleaning_summary.csv     record counts at each step and number of values imputed
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_ZIP = ROOT / "data" / "raw" / "route_801_direction_6_clean.zip"
OUT = ROOT / "data" / "processed"

COLUMNS = [
    "route_id", "current_route_id", "direction_code_id", "import_error", "import_trip_error",
    "transit_date_time", "open_date_time", "close_date_time", "bs_id", "vehicle_id",
    "ext_trip_id", "start_trip_time", "ons", "offs", "max_load", "dwell_time",
]
TERMINAL_STOPS = {"5304", "5873"}   # first and last stop; dwell there is layover time, not passenger service
COUNT_LIMIT = 40                    # ons/offs above this at one stop are counter errors (> 99.99th percentile)
DWELL_LIMIT_S = 600                 # dwell above 10 min at a non-terminal stop is not passenger service
HEADWAY_LIMIT_S = 3600              # gaps above 1 hour are service breaks or missing records, not headways
WINDOW_HOURS = (7, 18)              # weekday 7:00-17:59, when buses are scheduled every 10 minutes
SCHEDULED_HEADWAY_S = 600


def keep_rule(df):
    """The six filtering rules (route 801, direction 6, no errors, valid stop)."""
    return (
        (df.route_id == "801")
        & (df.route_id == df.current_route_id)
        & (df.import_error == "0")
        & (df.import_trip_error == "0")
        & (df.bs_id != "0")
        & (df.direction_code_id == "6")
    )


def load(raw_path):
    steps = []
    if raw_path:
        # Full raw file: read in chunks and apply the six rules one at a time so each step can be counted.
        counts = np.zeros(6, dtype=np.int64)
        total = 0
        parts = []
        for chunk in pd.read_csv(raw_path, usecols=COLUMNS, dtype=str, chunksize=1_000_000):
            total += len(chunk)
            m = chunk.route_id == "801"; counts[0] += m.sum()
            m &= chunk.route_id == chunk.current_route_id; counts[1] += m.sum()
            m &= (chunk.import_error == "0") & (chunk.import_trip_error == "0"); counts[2] += m.sum()
            m &= chunk.bs_id != "0"; counts[3] += m.sum()
            m &= chunk.direction_code_id == "6"; counts[4] += m.sum()
            parts.append(chunk[m])
        df = pd.concat(parts, ignore_index=True)
        steps += [
            ("Raw dataset (all routes)", total),
            ("Route 801 only", counts[0]),
            ("Bus serving its assigned route", counts[1]),
            ("No error flags", counts[2]),
            ("Valid stop ID", counts[3]),
            ("Southbound (direction 6)", counts[4]),
        ]
    else:
        # The zip is the raw file already filtered with the same six rules (counts from the dataset audit).
        df = pd.read_csv(RAW_ZIP, usecols=COLUMNS, dtype=str)
        assert keep_rule(df).all(), "zip should already satisfy the six filtering rules"
        steps += [
            ("Raw dataset (all routes)", 9_197_694),
            ("Route 801 only", 547_616),
            ("Bus serving its assigned route", 524_728),
            ("No error flags", 480_452),
            ("Valid stop ID (both directions)", 455_654),
            ("Southbound (direction 6)", len(df)),
        ]
    return df, steps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", help="path to the full raw APC CSV (optional)")
    args = ap.parse_args()

    df, steps = load(args.raw)

    # --- type conversion: every column arrives as text ---
    for c in ["ons", "offs", "max_load", "dwell_time"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["arrival"] = pd.to_datetime(df.open_date_time, format="%Y%m%d%H%M%S", errors="coerce")
    df["service_day"] = pd.to_datetime(df.transit_date_time.str[:8], format="%Y%m%d", errors="coerce")
    df = df.rename(columns={"bs_id": "stop_id", "ext_trip_id": "trip_id"})
    df = df.dropna(subset=["arrival", "service_day"])

    # --- duplicates: keep one record per trip per stop ---
    df = df.sort_values("arrival").drop_duplicates(["service_day", "trip_id", "stop_id"], keep="first")
    steps.append(("After removing duplicate stop records", len(df)))

    # --- stop order: median minutes after the trip's first stop, ranked ---
    first = df.groupby(["service_day", "trip_id"]).arrival.transform("min")
    df["min_from_start"] = (df.arrival - first).dt.total_seconds() / 60
    stops = (df.groupby("stop_id").agg(records=("arrival", "size"), median_min_from_start=("min_from_start", "median"))
               .sort_values("median_min_from_start").reset_index())
    stops["stop_order"] = np.arange(1, len(stops) + 1)
    stops["is_terminal"] = stops.stop_id.isin(TERMINAL_STOPS)
    df = df.merge(stops[["stop_id", "stop_order"]], on="stop_id")
    df["is_terminal"] = df.stop_id.isin(TERMINAL_STOPS)

    # --- time variables ---
    df["hour"] = df.arrival.dt.hour
    df["day_type"] = np.where(df.service_day.dt.dayofweek < 5, "Weekday", "Weekend")
    df["in_window"] = (df.day_type == "Weekday") & df.hour.between(WINDOW_HOURS[0], WINDOW_HOURS[1] - 1)

    # --- headway: time since the previous bus at the same stop on the same service day ---
    # Not every scheduled trip appears in the APC data, so a missing trip would look like a fake
    # 20-minute gap. A headway is therefore kept only when the two buses were scheduled exactly
    # 10 minutes apart (start_trip_time holds the scheduled start; its date part is not used).
    t = df.start_trip_time.str[8:14]
    df["scheduled_start_s"] = t.str[:2].astype(int) * 3600 + t.str[2:4].astype(int) * 60 + t.str[4:6].astype(int)
    df = df.sort_values(["service_day", "stop_id", "arrival"])
    by_stop = df.groupby(["service_day", "stop_id"])
    df["headway_s"] = by_stop.arrival.diff().dt.total_seconds()
    consecutive = by_stop.scheduled_start_s.diff().abs() == SCHEDULED_HEADWAY_S
    df.loc[~consecutive | (df.headway_s > HEADWAY_LIMIT_S) | df.is_terminal, "headway_s"] = np.nan

    # --- invalid values -> missing ---
    df["dwell_time_raw"] = df.dwell_time
    invalid = {
        "ons": df.ons > COUNT_LIMIT,
        "offs": df.offs > COUNT_LIMIT,
        "dwell_time": (df.dwell_time > DWELL_LIMIT_S) & ~df.is_terminal,
    }
    for c, mask in invalid.items():
        df.loc[mask, c] = np.nan
    df.loc[df.is_terminal, "dwell_time"] = np.nan   # layover, excluded from dwell analysis (not imputed)

    # --- imputation: median of the same stop and hour (fallback: stop median) ---
    imputed = {}
    for c in ["ons", "offs", "max_load", "dwell_time"]:
        need = df[c].isna() & ~(df.is_terminal & (c == "dwell_time"))
        df[c + "_imputed"] = need
        fill = df.groupby(["stop_id", "hour"])[c].transform("median")
        fill = fill.fillna(df.groupby("stop_id")[c].transform("median"))
        df.loc[need, c] = fill[need]
        imputed[c] = int(need.sum())

    # --- save ---
    OUT.mkdir(parents=True, exist_ok=True)
    keep = ["service_day", "arrival", "hour", "day_type", "in_window", "stop_id", "stop_order", "is_terminal",
            "vehicle_id", "trip_id", "ons", "offs", "max_load", "dwell_time", "dwell_time_raw", "headway_s",
            "ons_imputed", "offs_imputed", "max_load_imputed", "dwell_time_imputed"]
    df = df.sort_values(["service_day", "trip_id", "stop_order"])[keep]
    df.to_csv(OUT / "route801_events.csv.gz", index=False, date_format="%Y-%m-%d %H:%M:%S")
    stops.to_csv(OUT / "stops.csv", index=False)

    rows = [{"item": s, "value": int(n)} for s, n in steps]
    rows.append({"item": "Records in analysis window (weekdays 7:00-17:59)", "value": int(df.in_window.sum())})
    rows += [{"item": f"Values imputed: {c}", "value": n} for c, n in imputed.items()]
    rows.append({"item": "Terminal-stop records excluded from dwell analysis", "value": int(df.is_terminal.sum())})
    rows.append({"item": "Records with no valid headway (terminal stop, or previous bus not scheduled 10 min earlier)", "value": int(df.headway_s.isna().sum())})
    summary = pd.DataFrame(rows)
    summary.to_csv(OUT / "cleaning_summary.csv", index=False)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
