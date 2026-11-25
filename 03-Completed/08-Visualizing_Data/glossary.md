# 📚 Glossary: 08 - Visualizing Data

## 1️⃣ Matplotlib, Object-Oriented

**pyplot (`plt`)**  
Matplotlib's quick interface. Its calls act on a hidden "current" chart. In this module, use it only to create (`plt.subplots`) and show (`plt.show`) figures.

**Figure (`fig`)**  
The whole canvas. It holds one or more axes, and handles `suptitle`, layout, and saving.

**Axes (`ax`)**  
One chart inside a figure, with its own data, title, labels, limits, and ticks. (Not the same as an *axis*, the x or y line.)

**Object-Oriented Interface**  
Calling methods on explicit `fig` and `ax` objects (`ax.set_title()`) instead of pyplot functions (`plt.title()`).

**`plt.subplots(rows, cols)`**  
Creates a figure and an array of axes. `sharex=`/`sharey=` give every panel the same scale.

**`ax.set(...)`**  
Sets several properties at once: `title`, `xlabel`, `ylabel`, `xlim`, `ylim`, `xscale`, ...

**`layout='constrained'`**  
Automatically spaces panels so titles and labels don't overlap.

**Reference Line (`axvline`, `axhline`, `axvspan`)**  
A line (or shaded band) across the whole chart, often marking a statistic like the mean or an outlier fence.

**Log Scale (`set_xscale('log')`)**  
An axis where each step is a multiple (×10), not a fixed amount. Spreads out right-skewed data. Can't show zero.

**`np.geomspace()`**  
Evenly spaced numbers on a log scale. Used for histogram bins on a log axis.

**Tick Formatter**  
Controls how tick labels look: `StrMethodFormatter('£{x:,.0f}')` for money, `PercentFormatter(xmax=1)` for rates.

**`ax.annotate()`**  
Labels one point with text and an arrow. `xy=` is the point, and `xytext=` is where the text goes.

**`ax.bar_label()`**  
Writes each bar's value on (or above) the bar.

**Spines**  
The border lines around a chart. Removing the top and right spines reduces clutter.

**`fig.savefig()` / `plt.close(fig)`**  
Save the whole figure (call it before `plt.show()`), and free its memory (use it in loops).

**`plt.subplot_mosaic()`**  
Builds uneven panel layouts from a grid of names, and returns a dictionary of axes.

## 2️⃣ Plotting with Pandas

**`.plot.<kind>()`**  
Pandas' plotting methods (`line`, `bar`, `barh`, `hist`, `box`, `scatter`, `pie`). They draw with Matplotlib and return an `ax`.

**Index as x-axis**  
When pandas plots, the index supplies the x-values (or bar labels), and each column becomes one series.

**Grouped Bar Chart**  
Bars for several series side by side within each category, from a DataFrame like a `pivot_table`.

**100% Stacked Bar Chart**  
Bars stretched to the same length and divided by share, from a row-normalized `crosstab`. Shows composition.

**Wide Data**  
One column per series (`female`, `male`), with the x-values in the index. What pandas `.plot` expects.

**Long (Tidy) Data**  
One row per observation, with columns that name variables (`Sex`, `class`). What Seaborn expects.

**`.melt()`**  
Reshapes wide data into long data (the reverse of `pivot_table`).

## 3️⃣ Seaborn: Distributions

**Seaborn (`sns`)**  
A statistical plotting library built on Matplotlib. You map DataFrame columns to roles (`x`, `y`, `hue`, `col`, `row`).

**Axes-Level Function**  
Draws on one `ax` and accepts `ax=` (`histplot`, `boxplot`, `scatterplot`, ...).

**Figure-Level Function**  
Builds a whole figure with one panel per group (`displot`, `catplot`, `relplot`, `lmplot`). Sized with `height=` and `aspect=`, and returns a `FacetGrid`.

**`hue`**  
Splits the data by a column and gives each group its own color.

**`multiple=`**  
How `histplot` arranges `hue` groups: `'layer'`, `'stack'`, `'dodge'`, or `'fill'`.

**`stat=` / `common_norm=False`**  
Put a histogram on a relative scale (`'percent'`, `'density'`), and normalize each `hue` group separately, so groups of different sizes can be compared.

**Bimodal**  
A distribution with two peaks, often a sign that two groups are mixed together.

**KDE (Kernel Density Estimate)**  
A smoothed curve of a distribution. `bw_adjust=` controls the smoothing, and `cut=0` stops it at the data's range.

**ECDF**  
For each value, the share of data at or below it. Shows percentiles directly, with no bins or smoothing.

**Box Plot**  
Quartiles (box), median (line), whiskers to the last value inside the 1.5 × IQR fences, and outliers beyond them.

**Violin Plot**  
A mirrored KDE for each group, showing the full shape.

**Strip Plot / Jitter**  
Every point drawn individually, nudged randomly sideways so they don't overlap.

**Small Multiples**  
The same chart repeated in panels, one per group, on shared axes.

## 4️⃣ Seaborn: Relationships and Categories

**`style=` / `size=`**  
Encode extra columns in a scatter plot by marker shape and marker size.

**Overplotting**  
Points hiding each other where data are dense. Fix it with transparency (`alpha`), smaller points, or a log scale.

**`regplot` / `lmplot`**  
A scatter plot plus a fitted straight line (axes-level / figure-level). `ci=None` hides the uncertainty band, and `order=2` fits a curve.

**`countplot`**  
Bars of row counts per category.

**`barplot`**  
Bars of an estimate (the mean, by default) per category, with an error bar.

**`pointplot`**  
Estimates as points, connected across categories. Good for showing interactions.

**Confidence Interval (CI)**  
A range showing how much an estimate might change with a different sample. Seaborn's default error bar (`errorbar=('ci', 95)`).

**`errorbar=`**  
What a Seaborn error bar shows: `('ci', 95)`, `'se'` (standard error), `'sd'` (standard deviation), or `None`.

**Interaction**  
When the effect of one variable depends on another, as in non-parallel lines on a point plot.

**Heatmap**  
A table with each cell colored by its value. `annot=True` prints the numbers.

**Diverging Color Map**  
Two colors running out from a meaningful middle (`'vlag'`, `'coolwarm'`). Use it for correlations and differences, with `center=0`.

**Sequential Color Map**  
Light to dark for low to high (`'Blues'`, `'viridis'`). Use it for counts, rates, and amounts.

**`pairplot`**  
A scatter plot for every pair of numeric columns, with distributions on the diagonal. For exploration.

## 5️⃣ Choosing and Telling

**Exploration Chart vs. Communication Chart**  
Quick charts to find things out, vs. polished charts to show one finding to someone else.

**Zero Baseline**  
Bars and areas must start at zero, because they encode value by length.

**Highlight Color**  
One strong color for the item that matters, with everything else in gray.

**Colorblind-Safe Palette**  
Colors that stay distinguishable with common color-vision deficiencies (`sns.color_palette('colorblind')`).

**Palette Dictionary**  
A `{category: color}` dictionary passed as `palette=`, so each category keeps its color in every chart.

**Finding Title**  
A title that states the conclusion ("Sex Mattered More Than Class"), not just the contents ("Survival by Class and Sex").

**Direct Labeling**  
Putting labels next to the data (line ends, bar tops) instead of in a separate legend.

**`transform=ax.transAxes`**  
Positions text in axes coordinates, from (0, 0) at the bottom-left to (1, 1) at the top-right.
