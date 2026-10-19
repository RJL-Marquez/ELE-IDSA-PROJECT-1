# Results: hypothesis tests

All tests: weekdays 7:00–17:59, 126,070 stop events, 131 service days, **alpha = 0.05**.

## H1 — A longer gap means more passengers

![Passengers on board by headway group](../../figures/fig06_h1_load_vs_headway.png)

- Mean load doubles as the gap grows: **9.1 passengers** (0–5 min) → 11.0 → 13.4 → 15.8 → **17.9** (20+ min)
- Medians move the same way (8 → 17), so a few crowded buses are not driving it
- **Spearman:** rho = **0.349**, p < 0.001 (n = 51,437)
- **Kruskal-Wallis:** H = **5,883.4**, df = 4, p < 0.001 → **reject H₀**

## H2 — Passengers cost time at the stop

![Dwell time vs passengers boarding](../../figures/fig07_h2_dwell_vs_boardings.png)

- OLS (n = 116,697): **dwell = 12.79 + 6.91 × ons + 3.65 × offs** seconds
- Each **boarding adds ~6.9 s**, each alighting ~3.7 s — boarding costs **1.9×** more
- Mean dwell climbs from **16.9 s** at no boardings to **111.8 s** at 20 boardings
- Both p < 0.001 → **reject H₀**; R² = 0.180 (traffic and ramps explain the rest)

## H3 — Irregularity grows along the route

![Headway irregularity along the route](../../figures/fig08_h3_headway_cv_by_stop.png)

- Irregularity = CV (std ÷ mean of headways) per day and stop; 3,382 day × stop cells
- Mean CV rises from **0.39 at stop 2 to 0.58 at stop 28 (+51%)**, peak 0.62 at stop 27
- **Spearman:** rho = **0.955**, p < 0.001 (n = 27 stops) → **reject H₀**
- The 25th–75th band widens too: bad days get worse further down the line

## Discussion: one self-reinforcing cycle

- **H2 → H1:** more passengers → longer stops (+6.9 s each) → the bus falls behind
- **H1 → H2:** a bigger gap → more passengers waiting (9.1 → 17.9) → longer stops again
- **→ H3:** each turn amplifies the last, so spacing gets more uneven downstream (CV 0.39 → 0.58)
- Meanwhile the bus behind finds empty stops and catches up — **that is bunching**

## Limitations

- **Association, not proof of cause**
- **One route, one direction:** 801 southbound, weekdays 7:00–17:59, Jul–Dec 2021
- **APC counting errors:** sensors miscount at crowded doors
- **Missing trips:** only headways between buses scheduled 10 min apart were kept (51,437)
