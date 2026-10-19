# Why Buses Bunch: Passenger Demand and Bus Bunching on CapMetro Rapid Route 801

ELE IDSA Project 1 · GEC2B · Group 10 · Instructor: Ezron John D. Cabrera
Group 10: Khalil Badal, Elijah David Lopez, Rence Joseph Marquez

## Question

Is bus bunching on CapMetro Rapid Route 801 (Austin, Texas) related to passenger demand?

- **H1:** Buses with a longer gap behind the bus ahead carry more passengers.
- **H2:** The more people board and alight, the longer the bus stays at the stop.
- **H3:** Bus spacing becomes more irregular further along the route.

## Data

CapMetro *APC Raw July 2021 – December 2021*, Texas Open Data Portal, dataset
[`im6q-3pc9`](https://data.texas.gov/dataset/APC-Raw-July-2021-December-2021/im6q-3pc9).
Automatic passenger counter records, one row per bus per stop.

- `data/raw/route_801_direction_6_clean.zip`: Route 801 southbound records (229,421 rows), already filtered from the 9.2 M-row raw file with the six rules in `report/sections/02_methodology.md`.
- `data/processed/`: cleaned analysis dataset made by `src/prepare_data.py`.

## Repo layout

```
src/prepare_data.py      filter -> clean -> impute -> derive variables -> data/processed/
src/project.py           shared data loader + chart style (everyone imports this)
notebooks/               01 data preparation · 02 ridership patterns · 03 hypotheses
figures/                 all charts (PNG, 200 dpi)
report/sections/         report text, one Markdown file per section
TASKS.md                 who does what
CLAUDE.md                project context for Claude
```

## Run it

```bash
pip install -r requirements.txt
python src/prepare_data.py                 # rebuild data/processed/ (optional; it's committed)
python src/prepare_data.py --raw <path>    # or start from the full 3.7 GB raw CSV
jupyter notebook notebooks/
```
