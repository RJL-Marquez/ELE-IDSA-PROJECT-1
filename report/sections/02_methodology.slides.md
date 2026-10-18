# Methodology

## Data source

- **CapMetro** (Austin, Texas) *APC Raw July–December 2021*, Texas Open Data Portal (`im6q-3pc9`), free to download
- **APC** = automatic passenger counters: door sensors count boardings and alightings; GPS and clock record each stop
- **One row = one bus at one stop**; raw file: 9,197,694 rows × 47 columns, all routes
- **Study subset:** Route 801 southbound, Jul 1 – Dec 30, 2021: 229,421 records, 29 stops, 143 buses
- **Tools:** Python (pandas, Matplotlib, SciPy, statsmodels)

## Parameters used to segregate the data

| Parameter | Values used | Purpose |
|---|---|---|
| Route / direction | 801, southbound | Study route |
| Period | Jul 1 – Dec 30, 2021 | Full coverage |
| Day type | Weekday / weekend | Demand patterns |
| Analysis window | Weekdays 7:00–17:59 | Buses scheduled every 10 min |
| Hour of day | 0–23 | Demand by time |
| Stop order | 1 (first) to 29 (last) | Position on the route |
| Headway group | 0–5, 5–10, 10–15, 15–20, 20+ min | Close vs far-apart buses |

## Data cleaning

Records kept only if they pass all six filtering rules:

| Step | Rule | Records left |
|---|---|---|
| Raw | All routes | 9,197,694 |
| 1 | Route 801 | 547,616 |
| 2 | Bus serving its assigned route | 524,728 |
| 3–4 | No error flags | 480,452 |
| 5 | Valid stop ID | 455,654 |
| 6 | Southbound only | **229,421** |

![Dwell time before and after cleaning](../../figures/fig01_dwell_cleaning.png)

- **End stops (1, 29):** layovers, not service; 17,659 records left out of dwell and headway analysis
- **Invalid values:** >40 boardings at one stop, or dwell >10 min, marked missing
- **Imputation:** median of the same stop and hour (414 values, <0.2%)
- **Headways** kept only between buses scheduled 10 min apart, so unrecorded trips don't create fake gaps (51,437 valid)
