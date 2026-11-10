# 📝 Quiz: 08 - Visualizing Data

36 questions covering object-oriented Matplotlib, plotting with pandas, Seaborn distributions, Seaborn relationships and categories, and choosing and designing charts. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Matplotlib, Object-Oriented

**1.** (Short Answer) In `fig, ax = plt.subplots()`, what's the difference between `fig` and `ax`?

**2.** (Short Answer) Why does the object-oriented style scale better than `plt.title()`/`plt.xlabel()` calls when a figure has several charts?

**3.** (Code Tracing) How many axes does this create, and how do you reach the bottom-right one?
```python
fig, axes = plt.subplots(2, 3)
```

**4.** (Short Answer) What does `sharey=True` do, and why does it matter when comparing panels?

**5.** (Short Answer) When is a log-scale axis a good idea? What value can't it show?

**6.** (Multiple Choice) Which formatter displays `0.25` on an axis as `25%`?
A) `StrMethodFormatter('{x:.0%}')`  B) `PercentFormatter(xmax=1)`  C) `PercentFormatter(xmax=100)`  D) `ax.set(percent=True)`

**7.** (Short Answer) Why should you call `fig.savefig()` before `plt.show()`, and why `plt.close(fig)` inside a loop?

**8.** (Short Answer) In `ax.annotate('Peak', xy=(5, 10), xytext=(7, 12), arrowprops=...)`, what do `xy` and `xytext` each mean?

---

## Section B — Plotting with Pandas

**9.** (Short Answer) When pandas plots a DataFrame, what becomes the x-axis, and what becomes each line or set of bars?

**10.** (Code Tracing) What kind of chart does this draw, and what are the bar labels?
```python
titanic['Embarked'].value_counts().plot.barh()
```

**11.** (Short Answer) You plot a `pivot_table` with classes as the index and sexes as the columns. How do you switch the chart to group by sex instead?

**12.** (Short Answer) What does a 100% stacked bar chart show, and which `crosstab` argument produces the right table for it?

**13.** (Short Answer) What's the difference between wide and long data? Which does pandas `.plot` expect, and which does Seaborn expect?

**14.** (Short Answer) Should you sort the bars of an ordinal category (like ticket class) by value? Why or why not?

---

## Section C — Seaborn: Distributions

**15.** (Short Answer) What's the difference between an axes-level and a figure-level Seaborn function? Give one example of each.

**16.** (Short Answer) What does `hue='species'` do in `sns.histplot()`?

**17.** (Multiple Choice) Two groups have 500 and 50 rows. To compare the **shapes** of their distributions, use:
A) `stat='count'`  B) `multiple='stack'`  C) `stat='percent', common_norm=False`  D) `binwidth=1`

**18.** (Short Answer) Explain each part of a box plot: the box, the line inside it, the whiskers, and the dots.

**19.** (Short Answer) Name one thing a violin plot shows that a box plot hides, and one thing a strip plot shows that a violin hides.

**20.** (Short Answer) How do you read a group's median from an ECDF plot?

**21.** (True/False) A KDE curve always stays within the actual range of the data.

**22.** (Short Answer) Why does `showfliers=False` make sense when you draw a strip plot on top of a box plot?

---

## Section D — Seaborn: Relationships and Categories

**23.** (Short Answer) Name two ways to reduce overplotting in a scatter plot.

**24.** (Short Answer) In the penguins data, one `regplot` line through all the points slopes down, but one line per species slopes up. What's this called, and what's the lesson for fitting trend lines?

**25.** (Short Answer) Why did the four Anscombe datasets get identical lines from `lmplot`?

**26.** (Short Answer) What's the difference between `countplot` and `barplot`?

**27.** (Multiple Choice) `sns.barplot(..., errorbar='sd')` draws error bars showing:
A) the 95% confidence interval  B) the standard error  C) one standard deviation of the individual values  D) the IQR

**28.** (Short Answer) What does Seaborn's default error bar on a `barplot` represent?

**29.** (Short Answer) What does a `pointplot` with crossing or diverging lines tell you?

**30.** (Short Answer) Should a correlation heatmap use a diverging or a sequential color map? What about a heatmap of survival rates? Why?

---

## Section E — Choosing and Telling

**31.** (Short Answer) Why must bar charts start at zero, when line charts don't have to?

**32.** (Short Answer) Name the chart you'd choose for each: (a) the distribution of one numeric column, (b) the mix of categories within each group, (c) the relationship between two numeric columns.

**33.** (Short Answer) What's a palette dictionary, and why use one across a whole report?

**34.** (Short Answer) Rewrite this descriptive title as a finding title: "Mean Body Mass by Species."

**35.** (True/False) Every bar in a bar chart should have its own distinct color.

**36.** (Short Answer) Give two reasons to look at a chart **and** the matching numbers, rather than just one of them.

