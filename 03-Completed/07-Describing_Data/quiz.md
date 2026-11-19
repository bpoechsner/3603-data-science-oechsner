# 📝 Quiz: 07 - Describing Data

36 questions covering types of data, center and spread, shape and outliers, comparing groups, and relationships and correlation. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Types of Data

**1.** (Short Answer) What's the difference between a column's **dtype** and its **measurement scale**?

Dtype is how pandas stores the values (int64, str, bool). The measurement scale is what the values mean (nominal, ordinal, interval, ratio).

**2.** (Multiple Choice) Titanic's `Pclass` is stored as `1`, `2`, `3`. Its measurement scale is:
A) Nominal  B) Ordinal  C) Interval  D) Ratio

B

**3.** (Multiple Choice) Which scale has a true zero that means "none of it"?
A) Nominal  B) Ordinal  C) Interval  D) Ratio

D

**4.** (True/False) Temperature in °C is ratio data, because 20°C is twice 10°C.

False

**5.** (Short Answer) Is "number of siblings aboard" discrete or continuous? How can you tell?

Discrete. It’s a whole-number count, and you can’t have 2.5 siblings.

**6.** (Code Tracing) What prints?
```python
s = pd.Series([True, False, True, True])
print(s.mean())
```

0.75

**7.** (Short Answer) Why is `titanic['PassengerId'].mean()` meaningless, even though pandas computes it without complaint?

It’s an ID, a label that happens to be a number. An average of labels doesn’t measure anything.

**8.** (Short Answer) What does `ordered=True` in `pd.CategoricalDtype([...], ordered=True)` let you do that a plain `str` column can't?

It lets comparisons (>, <), .min() and .max(), and sorting follow your logical order instead of alphabetical order.

---

## Section B — Center and Spread

**9.** (Short Answer) Which is more robust to outliers, the mean or the median? Why?

The median. It depends only on the middle position, not on how far away the extreme values are.

**10.** (Code Tracing) What prints?
```python
s = pd.Series([2, 4, 4, 6, 100])
print(s.median(), s.mode()[0])
```

4.0 4

**11.** (Short Answer) A column's mean is much larger than its median. What does that suggest?

The data are right-skewed. A few large values are pulling the mean up.

**12.** (Multiple Choice) `pd.Series(data).std()` and `np.std(data)` give slightly different answers because:
A) NumPy rounds  B) pandas skips NaN  C) they use different default `ddof`  D) one is variance

C

**13.** (Short Answer) What's the IQR, and how do you compute it in pandas?

Q3 − Q1, the width of the middle half of the data: s.quantile(0.75) - s.quantile(0.25).

**14.** (Short Answer) In `.describe()`, a column's `count` is 714 but the DataFrame has 891 rows. What does that tell you?

177 values are missing. count only counts non-missing values.

**15.** (Short Answer) You fill 177 missing ages with the median age. What happens to the standard deviation, and why?

It shrinks. 177 identical values land right at the center, so the data look less spread out than they really are.

**16.** (Short Answer) Which spread statistic pairs naturally with the median, and which with the mean?

The IQR pairs with the median, and the standard deviation pairs with the mean.

---

## Section C — Shape and Outliers

**17.** (Multiple Choice) A column with `.skew()` of 4.8 is:
A) roughly symmetric  B) strongly left-skewed  C) strongly right-skewed  D) heavy-tailed but symmetric

C

**18.** (Short Answer) Write the formulas for the lower and upper fences of the 1.5 × IQR rule.

Lower = Q1 − 1.5 × IQR. Upper = Q3 + 1.5 × IQR.

**19.** (Short Answer) On Titanic fares, the IQR rule flags 116 values but the |z| > 3 rule flags only 20. Why are z-scores less sensitive on a skewed column?

Z-scores use the mean and std, and the outliers inflate both. The outliers stretch the yardstick measuring them, so fewer values look extreme.

**20.** (True/False) Any value flagged as an outlier should be removed before analysis.

False

**21.** (Short Answer) Name two things you can do with a real-but-extreme value instead of deleting it.

Use robust statistics (median, IQR), cap the value with .clip(), apply a log transform, or report it separately.

**22.** (Short Answer) Why can a value be an outlier within its group but not in the whole dataset (or the other way around)?

“Unusual” depends on what you compare against. A typical 1st-class fare looks extreme next to all passengers. A 2,700 g Chinstrap is normal overall but light for its species.

---

## Section D — Comparing Groups

**23.** (Short Answer) More 3rd-class passengers survived than 2nd-class passengers, but 3rd class had the lower survival rate. How can both be true?

3rd class was much bigger. More survivors in total doesn’t mean a higher share survived, so compare rates, not counts.

**24.** (Code Tracing) What does this compute?
```python
titanic.groupby('Sex')['Survived'].mean()
```

The survival rate (proportion who survived) for each sex.

**25.** (Multiple Choice) In `pd.crosstab(df['class'], df['Sex'], normalize='index')`, what adds up to 100%?
A) each row  B) each column  C) the whole table  D) nothing; it's counts

A

**26.** (Short Answer) What's the difference between what `pd.crosstab()` and `pivot_table()` compute?

crosstab counts combinations of two categorical columns. pivot_table computes any statistic (mean, median and so on) of a third column for each combination.

**27.** (Short Answer) Why should a group summary always include the group's size?

A rate or mean from a tiny group is unreliable. Size shows how much to trust the statistic.

**28.** (Short Answer) Cherbourg passengers survived at a higher rate than other ports. Explain how ticket class could be a **confounder** here.

About half of Cherbourg passengers were 1st class, and 1st class survived more. Class affects both the port mix and survival, so part of the port difference is really a class difference.

**29.** (Short Answer) What does `observed=True` do in a `groupby` on a categorical column?

It shows only the categories that actually have rows, and hides empty ones.

---

## Section E — Relationships and Correlation

**30.** (Short Answer) Why is covariance hard to interpret on its own, and how does correlation fix that?

Covariance depends on units (dividing a column by 10 divides the covariance by 10), so its size means nothing on its own. Correlation rescales it to a unitless −1 to 1.

**31.** (Multiple Choice) r = −0.85 means:
A) a weak negative linear relationship  B) a strong negative linear relationship  C) 85% of y is caused by x  D) no relationship

B

**32.** (Short Answer) Give two situations where Spearman is a better choice than Pearson.

Ordinal data, curved but always-rising relationships, and data with outliers or heavy skew. Any two of these work.

**33.** (True/False) If r = 0, the two columns have no relationship at all.

False

**34.** (Short Answer) Name three explanations for a correlation besides "A causes B."

Reverse causation (B causes A), a confounder (C causes both), and coincidence (especially after testing many pairs).

**35.** (Short Answer) What is Anscombe's quartet, and what lesson does it teach?

Four datasets with identical means, standard deviations and correlation (0.82) that look completely different when plotted. Summary statistics can hide structure, so always plot.

**36.** (Short Answer) In the penguins data, bill length and depth correlate at −0.24 overall but +0.39 to +0.65 within each species. What's this called, and what causes it here?

Simpson’s paradox. Species is the confounder: Gentoos have long but shallow bills, so pooling them with the shorter, deeper-billed species creates a negative trend that doesn’t exist within any one species.

