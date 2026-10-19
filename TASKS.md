# Tasks

| Person | Notebook | Figures | Report sections |
|---|---|---|---|
| **Rence** | `notebooks/01_data_preparation.ipynb` ✅ | `fig01_dwell_cleaning` ✅, `fig02_boardings_heatmap` ✅ | `02_methodology.md` ✅, `03b_results_heatmap.md` ✅, final assembly |
| **Elijah** | `notebooks/02_ridership_patterns.ipynb` ✅ | `fig03_boardings_by_hour` ✅, `fig04_daily_boardings` ✅, `fig05_headway_distribution` ✅ | `01_introduction.md` ✅, `03_results_ridership_patterns.md` ✅ |
| **Khalil** | `notebooks/03_hypotheses.ipynb` ✅ | `fig06_h1_load_vs_headway` ✅, `fig07_h2_dwell_vs_boardings` ✅, `fig08_h3_headway_cv_by_stop` ✅ | `05_results_hypotheses.md` ✅, `06_conclusion.md` ✅ |

The data is already cleaned. Everyone starts from `data/processed/route801_events.csv.gz` through `src/project.py`.

## How to start (everyone)

1. Get access to the repo. Rence adds you as a collaborator; accept the invite.
2. Open Claude Code on the repo. On claude.ai/code, start a session with `RJL-Marquez/ELE-IDSA-PROJECT-1`; on your laptop, use `git clone https://github.com/RJL-Marquez/ELE-IDSA-PROJECT-1` and run `claude` inside it.
3. Paste your prompt below.
   - **No repo access?** Download your pack from `handoff/` (`elijah_task_pack.zip` or `khalil_task_pack.zip`), unzip it and follow its `START_HERE.md`. It works in a normal claude.ai chat.
4. When it's done, look at your charts in `figures/` yourself. If a label is unclear or text overlaps, ask Claude to fix it.

---

## Elijah

**Paste this into Claude:**

```
Read CLAUDE.md, then do my tasks for this repo:

1. Create notebooks/02_ridership_patterns.ipynb (pip install -r requirements.txt first). Use the helpers in src/project.py and make these three charts:
   a) fig03_boardings_by_hour: average boardings per day for each hour of the day (0-23), one line for Weekday and one for Weekend (blue and orange), direct-label each line at its right end instead of a legend box. Y label "Average boardings per day", X label "Hour of day".
   b) fig04_daily_boardings: total boardings per service day from 2021-07-01 to 2021-12-30 (drop 2021-06-30, it is a partial day). Weekdays as a blue line, weekends as orange dots. Y label "Boardings per day", X label "Date". Mark any obvious holiday dips only if the data shows them.
   c) fig05_headway_distribution: histogram of headway in MINUTES (headway_s / 60) for window(ev), 1-minute bins from 0 to 40. Draw a dashed vertical line at 10 min labelled "Scheduled: 10 min". Compute and print the % of headways under 3 min ("bunched") and over 20 min ("long gap") and write those two numbers on the chart. Y label "Number of bus arrivals".
   Print the key numbers each chart is based on (peak hour and its value, weekday vs weekend average per day, average daily boardings, median headway, the two %s).
2. Write report/sections/01_introduction.md: short (about 200-250 words, bullets welcome) with
   - Background: where the data comes from (CapMetro Austin, APC sensors, Texas Open Data Portal, Route 801 = CapMetro Rapid, high-frequency service every 10 min on weekdays), what bus bunching is.
   - Motivation: why this dataset/topic matters (bunching makes riders wait longer, crowds some buses while others run empty; the dataset is large, real, free, stop-level).
   - Objective + the three hypotheses H1-H3 exactly as in CLAUDE.md.
3. Write report/sections/03_results_ridership_patterns.md: for each of my 3 figures, a heading, the figure filename, and 2-4 short bullets explaining what the chart shows, using only numbers printed by my notebook.
4. Commit only my files (notebook with outputs, 3 PNGs, 2 markdown files) and push to main (git pull --rebase origin main first).
```

---

## Khalil

**Paste this into Claude:**

```
Read CLAUDE.md, then do my tasks for this repo:

1. Create notebooks/03_hypotheses.ipynb (pip install -r requirements.txt first). Use the helpers in src/project.py. Use w = window(ev) for everything below.
   H1 (fig06_h1_load_vs_headway): keep rows with headway_s not null. Group headway into 0-5, 5-10, 10-15, 15-20, 20+ minutes. Box plot of max_load by group (no outlier dots), mark the mean of each group, show n under each box label. Y "Passengers on board", X "Headway (minutes since previous bus)". Tests: Spearman correlation headway_s vs max_load; Kruskal-Wallis across the 5 groups. Expect roughly: mean load rising from about 9 to about 18 passengers, rho about 0.35.
   H2 (fig07_h2_dwell_vs_boardings): rows with is_terminal == False. OLS with statsmodels: dwell_time ~ ons + offs; print the coefficient table and R squared. Chart: for ons = 0..20, plot the mean dwell time as points with a shaded 25th-75th percentile band, plus the fitted line (with offs at its mean). Y "Dwell time (seconds)", X "Passengers boarding at the stop".
   H3 (fig08_h3_headway_cv_by_stop): rows with headway_s not null. For each service_day and stop_order with at least 3 headways, compute CV = std/mean of headway_s; then average CV over days for each stop_order. Line chart with markers of mean CV vs stop_order (stops 2-28), with a shaded band for the 25th-75th percentile across days. Spearman correlation stop_order vs mean CV. Y "Headway irregularity (CV)", X "Stop order along the route". Expect CV rising from about 0.4 to about 0.6, rho about 0.9.
   Use alpha = 0.05. Print every statistic used in the text.
2. Write report/sections/05_results_hypotheses.md: one subsection per hypothesis with the figure filename, 3-4 bullets (what the chart shows with numbers, the test result with statistic and p-value, reject or fail to reject H0). Then a short "Discussion" with bullets: how H2 -> H1 -> H3 form one cycle (more passengers -> longer stops -> bus falls behind -> bigger gap -> even more passengers -> bunching grows along the route), and limitations (association, not proof of cause; one route and direction; APC counting errors; some trips not recorded).
3. Write report/sections/06_conclusion.md: 5-7 bullet points that summarize the WHOLE report (data used, cleaning, where and when demand is highest from report/sections/03b_results_heatmap.md, the three findings with key numbers, the overall conclusion, one recommendation such as holding control or faster boarding). If report/sections/03_results_ridership_patterns.md is still empty, add one bullet "[Ridership patterns: to be added from Elijah's section]". No paragraphs.
4. Commit only my files (notebook with outputs, 3 PNGs, 2 markdown files) and push to main (git pull --rebase origin main first).
```

---

## Rence (after Elijah and Khalil push)

- Review every figure against the rubric: labels, units, readability.
- Assemble the final report as slides or paper from `report/sections/*.md` and `figures/*.png`.
