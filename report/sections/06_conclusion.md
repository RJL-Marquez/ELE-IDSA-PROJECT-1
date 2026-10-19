# Conclusion

*Owner: Khalil*

- **Data:** CapMetro APC records (Texas Open Data Portal, dataset `im6q-3pc9`) for **Route 801 Rapid, southbound, 1 July – 30 December 2021** — 229,421 stop events at 29 stops from 9.2 million raw rows; the analysis window is weekdays 07:00–17:59, when buses are scheduled every 10 minutes (126,070 events, 131 service days).
- **Cleaning:** six filtering rules (route, assigned route, no error flags, valid stop, southbound), 7 duplicates dropped, 17,659 terminal records excluded because their "dwell" is layover time, impossible values (ons/offs above 40, dwell above 10 min) replaced by the stop-and-hour median — under 0.2% of records imputed — and only headways between buses scheduled exactly 10 minutes apart kept (51,437 valid headways).
- **Demand is concentrated, not spread out:** stop 1 is the busiest with about **442 boardings per weekday** (up to ~40 in a single hour, 07:00–10:00), followed by stop 5 (~329, peaking 06:00–09:00) and stop 19 (~204, peaking 15:00–17:00); stops after 20 are mostly alighting stops.
- **Ridership follows the commute:** weekdays average **2,514 boardings** vs **1,728** on weekends (+45%), peaking at 9:00 and 16:00; the median headway is **11.0 min** against a 10-min schedule, with **5.7%** of arrivals bunched (<3 min) and **10.3%** long gaps (>20 min).
- **All three hypotheses are supported** (alpha = 0.05):
  - **H1 — demand follows the gap:** mean load rises from **9.1 passengers** after a 0–5 min headway to **17.9** after 20+ min (Spearman rho = 0.349; Kruskal-Wallis H = 5,883.4, df = 4; both p < 0.001).
  - **H2 — passengers cost time:** every boarding adds about **6.9 s** and every alighting about **3.7 s** of dwell time (OLS, n = 116,697, R² = 0.180, p < 0.001); mean dwell goes from 16.9 s with no boardings to 111.8 s at 20 boardings.
  - **H3 — bunching grows along the route:** mean headway irregularity rises from **CV 0.39 at stop 2 to 0.58 at stop 28** (+51%, peak 0.62 at stop 27; Spearman rho = 0.955, p < 0.001).
- **Overall:** the three results close a self-reinforcing loop — more passengers → longer dwell → the bus falls behind → a bigger gap → still more passengers — so Route 801 does not keep its 10-minute spacing, and the unevenness is worst at the end of the route; the evidence is strong association, not proof of cause.
- **Recommendation:** break the loop early rather than late — apply **holding control** at a mid-route timing point (hold a bus that is running close behind the one ahead) and **speed up boarding** at the three heavy stops (1, 5 and 19) through all-door boarding or off-board fare payment, since boarding time is the single largest controllable term in the dwell model.
