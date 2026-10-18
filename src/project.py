"""Shared helpers: load the processed data and draw every chart in one consistent style.

In a notebook (inside notebooks/):
    import sys; sys.path.insert(0, "../src")
    from project import load_events, load_stops, window, new_fig, finish, save, COLORS, SEQ_CMAP
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"

# ---------------------------------------------------------------- data
def load_events(path=None):
    """One row per bus per stop (cleaned and imputed). See CLAUDE.md for the column list.
    Pass `path` if the CSV is not in data/processed/ (e.g. uploaded to a chat)."""
    return pd.read_csv(path or PROCESSED / "route801_events.csv.gz", parse_dates=["service_day", "arrival"])


def load_stops():
    """Stop IDs in route order (stop_order 1 = first stop)."""
    return pd.read_csv(PROCESSED / "stops.csv", dtype={"stop_id": str})


def window(df):
    """Analysis window: weekdays 7:00-17:59, when buses are scheduled every 10 minutes."""
    return df[df.in_window]


# ---------------------------------------------------------------- style
# Colours: use them in this order for categories; never pick random colours.
COLORS = {
    "blue": "#2a78d6",     # main series
    "orange": "#eb6834",   # second series / highlight
    "aqua": "#1baf7a",     # third series
    "text": "#0b0b0b",
    "muted": "#52514e",
    "grid": "#e4e3df",
}
SERIES = [COLORS["blue"], COLORS["orange"], COLORS["aqua"]]
# One-hue blue scale for heatmaps (light = low, dark = high).
SEQ_CMAP = LinearSegmentedColormap.from_list(
    "seq_blue", ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"])

plt.rcParams.update({
    "figure.dpi": 110,
    "savefig.dpi": 200,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "axes.titlesize": 16,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.titlepad": 12,
    "axes.labelsize": 13,
    "axes.labelcolor": COLORS["text"],
    "axes.edgecolor": COLORS["muted"],
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.axisbelow": True,
    "grid.color": COLORS["grid"],
    "grid.linewidth": 0.8,
    "xtick.color": COLORS["muted"],
    "ytick.color": COLORS["muted"],
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.frameon": False,
    "legend.fontsize": 12,
    "lines.linewidth": 2,
    "axes.prop_cycle": plt.cycler(color=SERIES),
})


def new_fig(width=10, height=5.6):
    """16:9 figure that fits a slide and a page. Returns (fig, ax)."""
    return plt.subplots(figsize=(width, height))


def finish(ax, title, xlabel, ylabel, note=None):
    """Title, axis labels (always with units) and an optional source/note line under the plot."""
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if note:
        ax.annotate(note, xy=(0, -0.18), xycoords="axes fraction", fontsize=10.5,
                    color=COLORS["muted"], ha="left", va="top")


def save(fig, name, folder=None):
    """Save to figures/<name>.png (200 dpi), or to `folder` if given."""
    out = Path(folder) if folder else FIGURES
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{name}.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    return path


SOURCE_NOTE = "Source: CapMetro APC data, Route 801 southbound, Jul–Dec 2021"
