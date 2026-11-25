# 📝 Quiz: 08 - Visualizing Data

36 questions covering object-oriented Matplotlib, plotting with pandas, Seaborn distributions, Seaborn relationships and categories, and choosing and designing charts. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Matplotlib, Object-Oriented

**1.** (Short Answer) In `fig, ax = plt.subplots()`, what's the difference between `fig` and `ax`?

fig is the whole figure, the canvas. ax is one chart on it.

**2.** (Short Answer) Why does the object-oriented style scale better than `plt.title()`/`plt.xlabel()` calls when a figure has several charts?

Each call goes to the exact ax you name, so with several charts nothing lands on the wrong one.

**3.** (Code Tracing) How many axes does this create, and how do you reach the bottom-right one?
```python
fig, axes = plt.subplots(2, 3)
```

6 axes (2 rows × 3 columns). The bottom-right one is axes[1, 2].

**4.** (Short Answer) What does `sharey=True` do, and why does it matter when comparing panels?

Every panel uses the same y-axis, so bar heights can be compared directly between panels.

**5.** (Short Answer) When is a log-scale axis a good idea? What value can't it show?

When the data is heavily right-skewed. It can't show zero, or negative values.

**6.** (Multiple Choice) Which formatter displays `0.25` on an axis as `25%`?
A) `StrMethodFormatter('{x:.0%}')`  B) `PercentFormatter(xmax=1)`  C) `PercentFormatter(xmax=100)`  D) `ax.set(percent=True)`

B

**7.** (Short Answer) Why should you call `fig.savefig()` before `plt.show()`, and why `plt.close(fig)` inside a loop?

Showing the figure can clear it, so save first. plt.close(fig) keeps the loop from piling up open figures.

**8.** (Short Answer) In `ax.annotate('Peak', xy=(5, 10), xytext=(7, 12), arrowprops=...)`, what do `xy` and `xytext` each mean?

xy is the point being labeled, and xytext is where the text goes.

---

## Section B — Plotting with Pandas

**9.** (Short Answer) When pandas plots a DataFrame, what becomes the x-axis, and what becomes each line or set of bars?

The index becomes the x-axis, and each column becomes its own line or set of bars.

**10.** (Code Tracing) What kind of chart does this draw, and what are the bar labels?
```python
titanic['Embarked'].value_counts().plot.barh()
```

A horizontal bar chart. The bar labels are the ports: S, C and Q.

**11.** (Short Answer) You plot a `pivot_table` with classes as the index and sexes as the columns. How do you switch the chart to group by sex instead?

Transpose the table with .T

**12.** (Short Answer) What does a 100% stacked bar chart show, and which `crosstab` argument produces the right table for it?

The mix of categories within each group. normalize='index'

**13.** (Short Answer) What's the difference between wide and long data? Which does pandas `.plot` expect, and which does Seaborn expect?

Wide has one column per series, and long has one row per observation. Pandas expects wide, and Seaborn expects long.

**14.** (Short Answer) Should you sort the bars of an ordinal category (like ticket class) by value? Why or why not?

No. Ordinal categories keep their natural order.

---

## Section C — Seaborn: Distributions

**15.** (Short Answer) What's the difference between an axes-level and a figure-level Seaborn function? Give one example of each.

Axes-level draws on one ax (histplot), and figure-level builds its own grid of panels (displot).

**16.** (Short Answer) What does `hue='species'` do in `sns.histplot()`?

It splits the data by species and colors each group.

**17.** (Multiple Choice) Two groups have 500 and 50 rows. To compare the **shapes** of their distributions, use:
A) `stat='count'`  B) `multiple='stack'`  C) `stat='percent', common_norm=False`  D) `binwidth=1`

C

**18.** (Short Answer) Explain each part of a box plot: the box, the line inside it, the whiskers, and the dots.

The box runs from Q1 to Q3, and the line inside is the median. The whiskers reach the last points inside the 1.5 × IQR fences, and the dots are the outliers.


**19.** (Short Answer) Name one thing a violin plot shows that a box plot hides, and one thing a strip plot shows that a violin hides.

A violin shows the full shape, such as a second peak. A strip plot shows every point and how many there are.

**20.** (Short Answer) How do you read a group's median from an ECDF plot?

Find where the group's curve crosses 0.5 on the y-axis.

**21.** (True/False) A KDE curve always stays within the actual range of the data.

False

**22.** (Short Answer) Why does `showfliers=False` make sense when you draw a strip plot on top of a box plot?

The strip plot already shows every point, so the outliers would appear twice.

---

## Section D — Seaborn: Relationships and Categories

**23.** (Short Answer) Name two ways to reduce overplotting in a scatter plot.

Transparency (alpha) and a log scale.

**24.** (Short Answer) In the penguins data, one `regplot` line through all the points slopes down, but one line per species slopes up. What's this called, and what's the lesson for fitting trend lines?

Simpson's paradox. Color by group before fitting a line.

**25.** (Short Answer) Why did the four Anscombe datasets get identical lines from `lmplot`?

They have the same means, variances and correlation, so the best-fit line comes out the same.

**26.** (Short Answer) What's the difference between `countplot` and `barplot`?

countplot counts rows per category. barplot shows a statistic (the mean by default) with error bars.

**27.** (Multiple Choice) `sns.barplot(..., errorbar='sd')` draws error bars showing:
A) the 95% confidence interval  B) the standard error  C) one standard deviation of the individual values  D) the IQR

C

**28.** (Short Answer) What does Seaborn's default error bar on a `barplot` represent?

A 95% confidence interval for the mean.

**29.** (Short Answer) What does a `pointplot` with crossing or diverging lines tell you?

An interaction: the effect of one variable depends on the other.

**30.** (Short Answer) Should a correlation heatmap use a diverging or a sequential color map? What about a heatmap of survival rates? Why?

Diverging for correlations, because 0 is a meaningful middle. Sequential for survival rates, which just run low to high.

---

## Section E — Choosing and Telling

**31.** (Short Answer) Why must bar charts start at zero, when line charts don't have to?

Bars show value by length, so a cut axis distorts them. Lines show value by position and slope.

**32.** (Short Answer) Name the chart you'd choose for each: (a) the distribution of one numeric column, (b) the mix of categories within each group, (c) the relationship between two numeric columns.

(a) histogram, (b) 100% stacked bar, (c) scatter plot.

**33.** (Short Answer) What's a palette dictionary, and why use one across a whole report?

A dictionary that maps each category to one color. It keeps the same category the same color in every chart.

**34.** (Short Answer) Rewrite this descriptive title as a finding title: "Mean Body Mass by Species."

"Gentoos Are About 1,350 g Heavier Than the Other Species"

**35.** (True/False) Every bar in a bar chart should have its own distinct color.

False

**36.** (Short Answer) Give two reasons to look at a chart **and** the matching numbers, rather than just one of them.

A chart can show patterns the numbers hide, like Anscombe or two groups mixed together. The numbers give exact values to check that the chart isn't misleading.

