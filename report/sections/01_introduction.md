# Introduction

*Owner: Elijah · Paper version*

## Background

The data for this study comes from the Capital Metropolitan Transportation Authority (CapMetro) in
Austin, Texas, published as *APC Raw July 2021 – December 2021* on the Texas Open Data Portal
(dataset `im6q-3pc9`) and free to download. The records are produced by automatic passenger
counters (APC): door sensors log how many passengers board and alight, while the bus's GPS and
onboard clock record where and when each stop takes place. Every row is therefore one bus at one
stop, which makes it possible to study the route stop by stop rather than as a daily total.

This study uses one slice of that dataset: Route 801 (CapMetro Rapid), southbound, from
1 July to 30 December 2021 — 229,414 stop events at 29 stops over 183 service days. Route 801 is a
high-frequency service scheduled every 10 minutes on weekdays from 7:00 to 18:00, which matters
because a constant planned headway gives a fixed benchmark to measure against.

**Bus bunching** is what happens when buses on such a route lose their even spacing and arrive in
pairs, followed by a long gap. The mechanism is self-reinforcing: a bus running slightly late finds
more riders waiting at each stop, spends longer at the kerb serving them, and falls further behind,
while the bus behind it catches up to an emptier stop. Passengers feel this as a long wait followed
by a crowded bus, even though the timetable has not changed.

## Motivation

Bunching degrades both reliability and fairness on a high-frequency route without any change to the
schedule or the size of the fleet, which makes it a problem worth understanding before money is
spent on either. This dataset is well suited to studying it: it is large (229,414 records), real,
free and recorded at stop level, so bunching can be measured directly instead of estimated. The
six-month window is long enough to cover seasonal variation, ordinary commuting patterns and
holiday disruption.

## Objectives and Hypotheses

This study examines how passenger demand relates to bus bunching on Route 801. Three hypotheses are
tested:

- **H1:** Buses with a longer gap behind the bus ahead (headway) carry more passengers.
- **H2:** The more people board and alight, the longer the bus stays at the stop (dwell time).
- **H3:** Headways become more irregular further along the route (bunching builds up).
