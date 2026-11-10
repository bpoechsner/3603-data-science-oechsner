# 📝 Quiz: 07 - Describing Data

36 questions covering types of data, center and spread, shape and outliers, comparing groups, and relationships and correlation. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Types of Data

**1.** (Short Answer) What's the difference between a column's **dtype** and its **measurement scale**?

**2.** (Multiple Choice) Titanic's `Pclass` is stored as `1`, `2`, `3`. Its measurement scale is:
A) Nominal  B) Ordinal  C) Interval  D) Ratio

**3.** (Multiple Choice) Which scale has a true zero that means "none of it"?
A) Nominal  B) Ordinal  C) Interval  D) Ratio

**4.** (True/False) Temperature in °C is ratio data, because 20°C is twice 10°C.

**5.** (Short Answer) Is "number of siblings aboard" discrete or continuous? How can you tell?

**6.** (Code Tracing) What prints?
```python
s = pd.Series([True, False, True, True])
print(s.mean())
```

**7.** (Short Answer) Why is `titanic['PassengerId'].mean()` meaningless, even though pandas computes it without complaint?

**8.** (Short Answer) What does `ordered=True` in `pd.CategoricalDtype([...], ordered=True)` let you do that a plain `str` column can't?

---

## Section B — Center and Spread

**9.** (Short Answer) Which is more robust to outliers, the mean or the median? Why?

**10.** (Code Tracing) What prints?
```python
s = pd.Series([2, 4, 4, 6, 100])
print(s.median(), s.mode()[0])
```

**11.** (Short Answer) A column's mean is much larger than its median. What does that suggest?

**12.** (Multiple Choice) `pd.Series(data).std()` and `np.std(data)` give slightly different answers because:
A) NumPy rounds  B) pandas skips NaN  C) they use different default `ddof`  D) one is variance

**13.** (Short Answer) What's the IQR, and how do you compute it in pandas?

**14.** (Short Answer) In `.describe()`, a column's `count` is 714 but the DataFrame has 891 rows. What does that tell you?

**15.** (Short Answer) You fill 177 missing ages with the median age. What happens to the standard deviation, and why?

**16.** (Short Answer) Which spread statistic pairs naturally with the median, and which with the mean?

---

## Section C — Shape and Outliers

**17.** (Multiple Choice) A column with `.skew()` of 4.8 is:
A) roughly symmetric  B) strongly left-skewed  C) strongly right-skewed  D) heavy-tailed but symmetric

**18.** (Short Answer) Write the formulas for the lower and upper fences of the 1.5 × IQR rule.

**19.** (Short Answer) On Titanic fares, the IQR rule flags 116 values but the |z| > 3 rule flags only 20. Why are z-scores less sensitive on a skewed column?

**20.** (True/False) Any value flagged as an outlier should be removed before analysis.

**21.** (Short Answer) Name two things you can do with a real-but-extreme value instead of deleting it.

**22.** (Short Answer) Why can a value be an outlier within its group but not in the whole dataset (or the other way around)?

---

## Section D — Comparing Groups

**23.** (Short Answer) More 3rd-class passengers survived than 2nd-class passengers, but 3rd class had the lower survival rate. How can both be true?

**24.** (Code Tracing) What does this compute?
```python
titanic.groupby('Sex')['Survived'].mean()
```

**25.** (Multiple Choice) In `pd.crosstab(df['class'], df['Sex'], normalize='index')`, what adds up to 100%?
A) each row  B) each column  C) the whole table  D) nothing; it's counts

**26.** (Short Answer) What's the difference between what `pd.crosstab()` and `pivot_table()` compute?

**27.** (Short Answer) Why should a group summary always include the group's size?

**28.** (Short Answer) Cherbourg passengers survived at a higher rate than other ports. Explain how ticket class could be a **confounder** here.

**29.** (Short Answer) What does `observed=True` do in a `groupby` on a categorical column?

---

## Section E — Relationships and Correlation

**30.** (Short Answer) Why is covariance hard to interpret on its own, and how does correlation fix that?

**31.** (Multiple Choice) r = −0.85 means:
A) a weak negative linear relationship  B) a strong negative linear relationship  C) 85% of y is caused by x  D) no relationship

**32.** (Short Answer) Give two situations where Spearman is a better choice than Pearson.

**33.** (True/False) If r = 0, the two columns have no relationship at all.

**34.** (Short Answer) Name three explanations for a correlation besides "A causes B."

**35.** (Short Answer) What is Anscombe's quartet, and what lesson does it teach?

**36.** (Short Answer) In the penguins data, bill length and depth correlate at −0.24 overall but +0.39 to +0.65 within each species. What's this called, and what causes it here?

