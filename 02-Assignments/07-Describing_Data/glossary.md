# 📚 Glossary: 07 - Describing Data

## 1️⃣ Types of Data

**dtype**  
How pandas *stores* a column (`int64`, `float64`, `str`, `bool`, `category`). It says nothing about what the values mean.

**Measurement Scale**  
What a column's values *mean*, and so which math is valid on them: nominal, ordinal, interval, or ratio.

**Qualitative (Categorical) Variable**  
Puts each row in a group or category (`Sex`, `species`, `Embarked`).

**Quantitative (Numeric) Variable**  
Measures or counts an amount (`Age`, `Fare`, `body_mass_g`).

**Discrete**  
Quantitative with countable values and gaps between them (number of siblings). Test: can you have 2.5 of it?

**Continuous**  
Quantitative that can take any value in a range (age, mass, length).

**Nominal**  
Categories with no order (eye color, port of embarkation). Allowed: counts, percentages, mode.

**Ordinal**  
Categories with an order but no guaranteed equal gaps (ticket class, star ratings, S/M/L). Adds: median, percentiles, ranking.

**Interval**  
Numeric with equal gaps but no true zero (°C, calendar year). Adds: differences, mean, std.

**Ratio**  
Numeric with equal gaps and a true zero meaning "none" (mass, price, age). Adds: ratios ("twice as much").

**Identifier**  
A column that labels rows (`PassengerId`). Stored as a number, but it isn't a quantity.

**`category` dtype**  
A pandas dtype for a fixed set of groups. Records that a column is categorical.

**Ordered Category (`pd.CategoricalDtype(..., ordered=True)`)**  
A category with a defined order, so `<`, `>`, `.min()`, `.max()`, and sorting follow *your* order instead of alphabetical order.

**Data Dictionary**  
A table describing every column of a dataset: its meaning, kind, scale, dtype, missing count, and distinct count.

## 2️⃣ Center and Spread

**Mean**  
The sum divided by the count. Sensitive to outliers.

**Median**  
The middle value after sorting (the 50th percentile). Robust to outliers.

**Mode**  
The most common value. `.mode()` returns a Series, because there can be ties.

**Robust Statistic**  
One that a few extreme values barely move (median, IQR, MAD).

**Range**  
max − min. Depends only on the two most extreme values.

**Variance**  
The average squared distance from the mean, in squared units.

**Standard Deviation (std)**  
The square root of the variance, in the original units. Roughly, how far a typical value is from the mean.

**`ddof`**  
"Delta degrees of freedom." `ddof=1` divides by n − 1 (a sample, and the pandas default). `ddof=0` divides by n (a whole population, and the NumPy default).

**Percentile / Quantile**  
The value that a given share of the data falls below. `.quantile(0.9)` is the 90th percentile.

**Quartiles (Q1, Q2, Q3)**  
The 25th, 50th, and 75th percentiles.

**Interquartile Range (IQR)**  
Q3 − Q1: the width of the middle half of the data. Robust.

**`skipna`**  
Pandas statistics skip missing values by default, so a mean is the mean of the *known* values.

## 3️⃣ Shape and Outliers

**Distribution**  
The pattern of how often each value (or range of values) occurs.

**Symmetric**  
Both sides of the distribution mirror each other. Mean ≈ median.

**Right-Skewed (Positive Skew)**  
A long tail of large values. Mean > median (incomes, prices).

**Left-Skewed (Negative Skew)**  
A long tail of small values. Mean < median.

**Skewness (`.skew()`)**  
A number for lopsidedness. Roughly: |skew| < 0.5 is symmetric, 0.5–1 is moderate, and > 1 is strong.

**Kurtosis (`.kurt()`)**  
How heavy the tails are. Pandas reports *excess* kurtosis, so a bell curve is about 0.

**Outlier**  
A value far from most of the others. Unusual, but not necessarily wrong.

**IQR Fences (1.5 × IQR Rule)**  
Flag values below Q1 − 1.5·IQR or above Q3 + 1.5·IQR. Robust, and the rule box plots use.

**Z-Score**  
(value − mean) / std: how many standard deviations a value is from the mean. |z| > 3 is a common flag. Not robust on skewed data.

**Log Transform (`np.log1p`)**  
Takes log(1 + x) to squeeze a long right tail. It changes the scale, not the rows.

**Capping / Winsorizing (`.clip()`)**  
Setting values beyond a cutoff *to* the cutoff, instead of removing them.

## 4️⃣ Comparing Groups

**Rate / Proportion**  
A count divided by its group size. Compare groups of different sizes with rates, not counts.

**`pd.crosstab()`**  
Counts every combination of two categorical columns. `normalize='index'`, `'columns'`, or `'all'` turns counts into shares. `margins=True` adds totals.

**`pivot_table()`**  
Computes any statistic (`aggfunc=`) of one column for every combination of two others.

**`observed=True`**  
In a `groupby` on a categorical column, shows only the categories that actually appear.

**Confounder (Confounding Variable)**  
A third variable tangled up with both the group and the outcome, making a difference look like it's caused by the group (class behind the port-of-embarkation survival gap).

**Percentage Points**  
The difference between two percentages (97% − 50% = 47 percentage points), as opposed to a relative change.

## 5️⃣ Relationships

**Covariance (`.cov()`)**  
Whether two columns move together. Its size depends on the units, so it's hard to interpret.

**Correlation (Pearson's r, `.corr()`)**  
Covariance rescaled to −1…1 with no units. Measures **linear** association only.

**Correlation Matrix**  
`df.corr()`: r for every pair of columns. It's symmetric, with 1s on the diagonal.

**Spearman Correlation (ρ, `method='spearman'`)**  
Pearson's r computed on ranks. Use it for ordinal data, curved-but-monotonic relationships, and data with outliers.

**Monotonic**  
Always rising (or always falling), though not necessarily in a straight line.

**Correlation ≠ Causation**  
An association can come from A → B, B → A, a confounder, or coincidence.

**Spurious Correlation**  
A correlation that arises by chance, especially when many pairs are tested and only the strongest is reported.

**Anscombe's Quartet**  
Four datasets with identical means, standard deviations, and correlation that look completely different when plotted.

**Simpson's Paradox**  
A relationship that reverses (or vanishes) when groups are combined. In the penguins, bill length and depth correlate positively within every species but negatively overall.
