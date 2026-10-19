# Results: Ridership Patterns

*Owner: Elijah · Notebook: `notebooks/02_ridership_patterns.ipynb`*

## Boardings by hour of day

`fig03_boardings_by_hour.png`

- Weekday demand peaks at **9:00** with **195.9 average boardings**, then stays high through the afternoon with a second peak at **16:00 (175.9)**, matching the morning and afternoon commute.
- Weekend demand is lower and flatter, peaking at **15:00** with **124.6 average boardings**, about 36% below the weekday morning peak.
- Average total boardings per weekday (**2,514**) are 45% higher than on weekends (**1,728**), which suggests Route 801 is mainly a commuter service.
- Both day types have almost no ridership between 1:00 and 4:00, with a sharp weekday ramp-up from 5:00.

---

## Boardings per service day

`fig04_daily_boardings.png`

- Average boardings per service day over the study period: **2,291** (weekdays **2,514**, weekends **1,728**).
- Weekday ridership is highest in **October** (average **3,025** per weekday) and lowest in July, August and November (about **2,350**). The October rise may reflect students and office workers returning in the fall, but the data alone can't confirm that.
- The clearest holiday dip is **Thanksgiving (Nov 25, 2021)**: **1,146** boardings, less than half the weekday average and 3.8 standard deviations below it.
- Weekend ridership (orange dots) stays below weekday ridership throughout. The lowest day is **Christmas Day (Dec 25)** with **871** boardings.

---

## Headway distribution (analysis window)

`fig05_headway_distribution.png`

- Of the 51,437 valid headways in the analysis window (weekdays 7:00–17:59), the **median is 11.0 minutes**, just above the scheduled 10 minutes.
- The distribution has a long right tail: **10.3% of headways exceed 20 minutes** (long gaps) and **5.7% are under 3 minutes** (bunched buses).
- The most common headway is **8–9 minutes**, followed by 10–11 minutes, so many buses do run close to schedule, but when spacing breaks down the gaps are large.
- Together, roughly **1 in 6 bus arrivals** is either bunched or a long gap.
