# Introduction

## Background

- **Data:** CapMetro (Austin, Texas) automatic passenger counter (APC) records, Texas Open Data Portal, free and public
- **Route 801 (CapMetro Rapid):** scheduled every **10 minutes** on weekdays 7:00–18:00
- **Bus bunching:** buses lose their even spacing and arrive in pairs, then a long gap
- A late bus finds more riders, dwells longer and falls further behind, while the bus behind catches up

## Motivation and hypotheses

- Bunching makes riders wait longer and crowds some buses while others run nearly empty
- The dataset is large (229,421 stop records), real and stop-level, so bunching can be measured directly
- **H1:** Buses with a longer gap behind the bus ahead (headway) carry more passengers.
- **H2:** The more people board and alight, the longer the bus stays at the stop (dwell time).
- **H3:** Headways become more irregular further along the route (bunching builds up).
