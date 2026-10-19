# Presentation Script: Why Buses Bunch

ELE IDSA Project 1 · GEC2B · Group 10
Speaking order: **Elijah** (slides 1–4, 8, 9, 11) · **Rence** (slides 5–7, 10) · **Khalil** (slides 12–17)

Each slide takes about 30–60 seconds, so the whole talk runs about 12–15 minutes. You don't need to read word for word. The **bold** parts are the numbers to say exactly.

---

## 1 · Title (Elijah)

Good [morning/afternoon]. We're Group 10: Khalil Badal, Elijah David Lopez and Rence Joseph Marquez. Our project is called *Why Buses Bunch*. We used real bus data from Austin, Texas, to check whether passenger demand is linked to bus bunching on one of their busiest routes, Route 801.

## 2 · Bus bunching: the problem (Elijah)

First, what is bus bunching? Imagine buses that leave 10 minutes apart. If one bus runs a little late, more people have piled up at the next stops. It takes longer to load them, so the bus falls even further behind. The bus behind it finds fewer people waiting, moves faster and catches up. In the end the two buses travel together, one packed and one almost empty, followed by a long gap with no bus at all. This was first described by Newell and Potts in 1964, and it's still a common problem on frequent bus routes.

## 3 · The dataset (Elijah)

Our data comes from CapMetro, the public transit agency of Austin, Texas. Their buses have automatic passenger counters: sensors at the doors count people getting on and off, and the bus's GPS and clock record when and where every stop happens. Each row in the data is one bus stopping at one stop.

We focused on Route 801, a rapid line scheduled **every 10 minutes** on weekdays. We used the southbound direction from **July 1 to December 30, 2021**. That's **229,421 stop records** across **29 stops** and **143 buses**. We chose it because it's large, real, free and detailed enough to measure bunching directly.

## 4 · Objective and hypotheses (Elijah)

Our objective is to find out whether passenger demand is related to bus bunching on this route. We test three hypotheses:

- **H1:** buses with a longer gap behind the bus ahead carry more passengers.
- **H2:** the more people board and get off, the longer the bus stays at the stop.
- **H3:** the spacing between buses gets more irregular further along the route.

Two terms we'll use a lot. **Headway** is the time since the previous bus at the same stop. **Dwell time** is how long the doors stay open. All tests use a 5% significance level. I'll pass it to Rence for the methodology.

## 5 · How we processed the data (Rence)

Thanks. The raw file has about **9.2 million rows**, covering every CapMetro route. We applied **six filters**:

- Route 801 only
- the bus is actually serving its assigned route
- no error flag on the record
- no error flag on the trip
- a valid stop ID
- southbound only

That leaves **229,421 records**. We then fixed **414** impossible values, less than **0.2%** of the data. That gave us **51,437** valid headways in our analysis window: weekdays from 7 AM to 6 PM, when buses are scheduled every 10 minutes.

One important check: some trips are missing from the data. If a bus wasn't recorded, the next one looks like it came 20 minutes after the previous bus, which is a fake gap. So we only count a headway when the two buses were scheduled exactly 10 minutes apart.

## 6 · Parameters (Rence)

This table lists the parameters we used to group the data.

- **Route and direction** set the study route.
- **Period** covers the full six months.
- **Day type** lets us compare weekdays and weekends.
- **Analysis window** keeps only the hours with a constant 10-minute schedule, so any irregularity comes from how the buses actually run, not from the timetable.
- **Hour of day** and **stop order** show when and where things happen.
- **Headway groups** let us compare buses that are close together with buses that are far apart.

## 7 · Data cleaning (Rence)

Here's the cleaning in more detail. The top chart shows dwell time before cleaning. There's a long tail past 10 minutes, some even reaching hours. Those come from the two end stops, where buses wait between trips. That's a layover, not passengers boarding, so we left those **17,659** records out of the dwell and headway analysis.

We also treated more than **40** boardings at one stop, or doors open longer than **10 minutes** at a normal stop, as counter errors. We replaced those with the median for the same stop and hour. We used the median because the data is very skewed. The bottom chart is the cleaned result. Elijah will now show the ridership patterns.

## 8 · Ridership by hour (Elijah)

This chart shows average boardings per day for each hour. On weekdays, the blue line, there are two peaks: **9 AM** with about **196** boardings and **4 PM** with about **176**. That matches the morning and evening commute. Weekends, the orange line, are lower and flatter, peaking at **3 PM**, about **36%** below the weekday peak. Overall, a weekday averages **2,514** boardings, **45%** more than a weekend day's **1,728**. So this is mainly a commuter route.

## 9 · Boardings per day (Elijah)

Here are the total boardings for every day of the six months. Weekdays are the blue line and weekends are the orange dots. Ridership is highest in **October**, with about **3,025** boardings per weekday. The two lowest points are holidays. Thanksgiving had only **1,146** boardings, less than half a normal weekday. Christmas Day had **871**, the lowest of the whole period.

## 10 · Where people board (Rence)

This heatmap combines the two views. Each row is a stop along the route, each column is an hour, and darker means more boardings. Stop 1, the first stop, is by far the busiest, with about **442** boardings per weekday, heaviest from 7 to 10 AM. Stop 5 is busy in the morning and stop 19 in the afternoon. Most stops near the end of the route see few boardings, because people are mostly getting off there. The key point is that demand is very uneven. A bus that reaches a busy stop at a busy hour has many more people to serve.

## 11 · How spaced out the buses are (Elijah)

Now the spacing itself. The schedule says 10 minutes, and the median gap we measured is **11 minutes**, so on paper it's close. But look at the spread. **5.7%** of arrivals came less than 3 minutes after the previous bus, which is bunching. **10.3%** came more than 20 minutes after, which is a long gap. Together that's about **1 in 6** arrivals. Khalil will now show whether this is linked to passenger demand.

## 12 · H1: longer gap, more passengers (Khalil)

Thanks. Our first hypothesis is that buses with a longer gap carry more passengers. We grouped every arrival by its headway. When a bus came within 5 minutes of the previous one, it averaged **9.1** passengers on board. When the gap was over 20 minutes, it averaged **17.9**, almost double. The medians follow the same pattern, so it's not just a few crowded buses. The Spearman correlation is **0.35**, and the Kruskal–Wallis test gives a p-value below **0.001**. So we reject the null hypothesis: the load depends on the gap.

## 13 · H2: passengers cost time (Khalil)

Our second hypothesis is that more passengers mean longer stops. We fitted a linear regression of dwell time on boardings and alightings. Each passenger boarding adds about **6.9 seconds**, and each passenger getting off adds about **3.7 seconds**. Boarding takes almost twice as long, which makes sense because people pay at the front door. Both effects are significant, with p below **0.001**. The R-squared is **0.18**, which means passengers explain part of the dwell time; the rest comes from things like traffic and wheelchair ramps. We reject the null hypothesis.

## 14 · H3: bunching builds up (Khalil)

Our third hypothesis is that bunching builds up along the route. For every stop and day, we measured how irregular the gaps were using the coefficient of variation, which is the standard deviation divided by the mean. Zero would mean perfect spacing. At stop 2 it's **0.39**, and by stop 28 it's **0.58**, a **51%** increase. The Spearman correlation between stop order and irregularity is **0.96**, almost a straight line up, with p below **0.001**. So we reject the null hypothesis: buses drift off their spacing the further they go.

## 15 · The bunching loop (Khalil)

Putting it together, the three results form a loop.

1. More passengers waiting means longer stops. That's H2.
2. Longer stops make the bus fall behind.
3. Falling behind widens the gap to the bus ahead.
4. A bigger gap means even more passengers waiting. That's H1.

Each turn of the loop makes it worse, which is why the spacing gets more irregular along the route, which is H3.

Some limitations. This shows association, not proof of cause. It covers one route, one direction, weekday daytime only, in 2021. And the passenger counters can miscount, and some trips weren't recorded.

## 16 · Conclusion (Khalil)

To conclude:

- Demand on Route 801 is concentrated at **stops 1, 5 and 19**, and at **9 AM and 4 PM**.
- Buses that come after a long gap carry about **twice** the passengers.
- Each boarding adds almost **7 seconds** at the stop.
- The spacing gets steadily worse along the route.
- All three null hypotheses were rejected.

Our recommendation is to break the loop early. Hold buses at a mid-route stop to restore even spacing, and speed up boarding at the busiest stops, for example with all-door boarding or paying before getting on.

## 17 · Thank you (Khalil)

That's our project. Thank you for listening; we're happy to take questions.

---

## Q&A prep

**Why data from Austin and not the Philippines?**
We tried to get EDSA Busway data, but no stop-level records like this are publicly available. CapMetro publishes theirs for free, and the bunching mechanism is the same on any high-frequency route.

**Why the median and not the mean for imputation?**
Boardings and dwell times are heavily skewed: most stops are short, with a few very long ones. The mean would be pulled up by those extremes, while the median reflects a typical value. Only 414 values (<0.2%) were imputed, so it barely affects the results.

**Why Spearman and Kruskal–Wallis instead of Pearson or ANOVA?**
The data isn't normally distributed. Passenger counts are whole numbers and skewed. These rank-based tests don't assume normality.

**R² is only 0.18. Isn't that weak?**
It means passengers explain part of the dwell time, not all of it. Traffic, wheelchair ramps and driver behaviour also matter. But the effect itself is strong and significant: about 6.9 s per boarding, p < 0.001.

**Does this prove demand causes bunching?**
No. It shows a strong association that fits the known bunching mechanism. A late bus gets more passengers, and more passengers make a bus later, so the relationship runs both ways. Proving cause would need an experiment or a simulation.

**Why only southbound?**
To keep one consistent direction and stop order. The same cleaning rules also give a dataset for the other direction (226,233 records), which could be a follow-up.

**What's the "fake gap" problem?**
Some scheduled trips aren't in the data. Without a fix, a missing bus makes the next one look 20 minutes late. We only measured gaps between buses scheduled exactly 10 minutes apart.
