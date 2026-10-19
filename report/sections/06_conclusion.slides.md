# Conclusion

## What we studied

- **Data:** CapMetro APC records, Route 801 Rapid southbound, Jul 1 – Dec 30 2021 — **229,421 stop events**, 29 stops, from 9.2 million raw rows
- **Window:** weekdays 7:00–17:59, when buses run every 10 min (126,070 events, 131 days)
- **Cleaning:** six filtering rules, end-stop layovers removed, impossible values imputed (<0.2%), **51,437 verified headways**
- **Demand is concentrated:** stop 1 ~429 boardings per weekday, stop 5 ~323 (morning), stop 19 ~201 (afternoon)
- *[Ridership patterns: to be added from Elijah's section]*

## What we found

- **H1 — demand follows the gap:** mean load **9.1 → 17.9 passengers** as headway grows (rho = 0.349, p < 0.001)
- **H2 — passengers cost time:** **+6.9 s per boarding**, +3.7 s per alighting (n = 116,697, p < 0.001)
- **H3 — bunching builds up:** headway irregularity **CV 0.39 → 0.58** along the route (rho = 0.955, p < 0.001)
- **All three hypotheses are supported** at alpha = 0.05

## Conclusion and recommendation

- The three results close one loop: **more passengers → longer stops → bigger gap → still more passengers**
- Route 801 does not hold its 10-minute spacing, and the unevenness is **worst at the end of the route**
- The evidence is a strong association, **not proof of cause**
- **Recommendation:** break the loop early — **holding control** at a mid-route timing point, and **faster boarding** at stops 1, 5 and 19 (all-door boarding or off-board fare payment)
