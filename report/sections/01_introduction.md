# Introduction

*Owner: Elijah*

## Background

- **Data source:** Capital Metropolitan Transportation Authority (CapMetro), Austin, Texas — *APC Raw July 2021 – December 2021*, Texas Open Data Portal (ID `im6q-3pc9`), free and public.
- **Collection:** automatic passenger counters (APC) use door sensors to log boardings and alightings; GPS and an onboard clock record the time and stop for each event. One row = one bus at one stop.
- **Study subset:** Route 801 (CapMetro Rapid), southbound, July 1 – December 30, 2021 — 229,421 stop events, 29 stops, 183 service days. Scheduled every **10 minutes** on weekdays 7:00–18:00.
- **Bus bunching:** buses lose their even spacing and arrive in pairs, followed by a long gap. A late bus finds more riders waiting, dwells longer, and falls further behind; the bus behind it catches up. Some riders wait far longer than scheduled; some buses are crowded while others run nearly empty.

## Motivation

- Bunching degrades reliability and equity on high-frequency routes without any change to the schedule or fleet.
- The Route 801 APC dataset is large (229,421 records), real, free, and stop-level — it enables direct measurement of bunching rather than estimation.
- The six-month window captures seasonal variation, commuting patterns, and holiday disruptions.

## Objectives and Hypotheses

This study examines how passenger demand relates to bus bunching on Route 801. Three hypotheses are tested:

- **H1:** Buses with a longer gap behind the bus ahead (headway) carry more passengers.
- **H2:** The more people board and alight, the longer the bus stays at the stop (dwell time).
- **H3:** Headways become more irregular further along the route (bunching builds up).
