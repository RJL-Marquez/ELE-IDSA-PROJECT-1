# CLAUDE.md: ELE IDSA Project 1 (Group: Rence, Khalil, Elijah)

Read this first. It has everything you need, so you don't have to explore the repo.

## The project

Data Science and Analytics report (instructor: Ezron John D. Cabrera, section GEC2B).
**Topic:** *Why Buses Bunch: the relationship between passenger demand and bus bunching on CapMetro Rapid Route 801 (Austin, Texas), July–December 2021.*

**Hypotheses**
- **H1:** Buses with a longer gap behind the bus ahead (headway) carry more passengers.
- **H2:** The more people board and alight, the longer the bus stays at the stop (dwell time).
- **H3:** Headways become more irregular further along the route (bunching builds up).

**What the instructor grades (rubric weight)**
- Introduction/Motivation ×2: clear background, short.
- Methodology ×2: parameters defined, acquisition and cleaning explained **without being wordy**.
- **Results & Discussion ×4: correct, readable, good-looking plots (axis labels, units, tick marks).**
- Conclusion ×2: **bullet points** that summarize the whole report.

The final format (slides or paper) is not decided yet. Write every section as **short Markdown with bullets**, so it can go either way.

## Data (already cleaned; do NOT re-clean)

```python
import sys; sys.path.insert(0, "../src")        # from inside notebooks/
from project import load_events, load_stops, window, new_fig, finish, save, COLORS, SERIES, SEQ_CMAP, SOURCE_NOTE
ev = load_events()      # one row per bus per stop, 229,414 rows
w  = window(ev)         # analysis window: weekdays 7:00-17:59 (buses scheduled every 10 min)
```

| Column | Meaning |
|---|---|
| `service_day`, `arrival` | service date; time the doors opened |
| `hour`, `day_type`, `in_window` | hour 0–23; "Weekday"/"Weekend"; True if weekday 7:00–17:59 |
| `stop_id`, `stop_order`, `is_terminal` | stop ID; position 1 (first) to 29 (last); True for stops 1 and 29 |
| `vehicle_id`, `trip_id` | bus and trip IDs |
| `ons`, `offs` | passengers boarding / alighting at this stop |
| `max_load` | passengers on board after the stop |
| `dwell_time` | seconds doors were open (cleaned; NaN at terminal stops) |
| `dwell_time_raw` | dwell before cleaning (only for the before/after figure) |
| `headway_s` | seconds since the previous bus at this stop; NaN when not valid (terminal stops, first bus, or the previous recorded bus was not scheduled 10 min earlier) |
| `*_imputed` | True if that value was imputed |

## Rules

1. **Charts:** always use `new_fig()`, `finish(ax, title, xlabel, ylabel, note=SOURCE_NOTE)` and `save(fig, "figNN_name")`.
   - Every axis label has units, e.g. "Headway (minutes)" or "Passengers on board".
   - Use the colours from `COLORS`/`SERIES` only, in order: blue, orange, aqua.
   - No dual y-axes.
   - Never put a number on every bar or point; label only what matters.
2. **Only edit your own files** (listed in TASKS.md). Don't touch other people's notebooks or sections, `src/`, or `data/`.
3. **Every number in the text must come from your notebook output.** Never estimate or invent numbers.
4. **Keep text short:** bullets and 1–3 sentence paragraphs. The rubric penalizes wordiness.
5. **Commit only your files.** Before pushing, run `git pull --rebase origin main`.
6. **Saving notebooks:** save them with their outputs, so the charts and numbers stay visible on GitHub.
