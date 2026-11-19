# 🔢 Module 07: Describing Data

Module 06 got your data into shape. This module asks what the data actually **say**: what each column means, what's typical, how much things vary, which values are unusual, how groups differ, and which columns move together. You'll do it all with pandas and numbers alone, and you'll find out what numbers alone can miss. Module 08 picks up from there with charts.

All notebooks use **local data files in this folder** (`titanic.csv` and `pokemon.csv` from Module 06, plus `penguins.csv` and `anscombe.csv`), so nothing downloads over the network.

---

## 🗂 Notebook Overview

| Notebook | Description |
|----------|-------------|
| [01-Types_of_Data.ipynb](01-Types_of_Data.ipynb) | **dtype vs. meaning**: qualitative/quantitative, discrete/continuous, the four scales (nominal, ordinal, interval, ratio), recording meaning with `category`, ordered `CategoricalDtype`, and `bool`, why the mean of a True/False column is a proportion, and building a **data dictionary**. Saves to `01-OutputFiles`. |
| [02-Center_and_Spread.ipynb](02-Center_and_Spread.ipynb) | `.mean()`/`.median()`/`.mode()` and robustness, range/variance/std, `ddof` (why pandas and NumPy disagree), percentiles and the IQR, reading `.describe()` row by row, summarizing text columns, and how filling missing values shrinks the spread. |
| [03-Shape_and_Outliers.ipynb](03-Shape_and_Outliers.ipynb) | Symmetric vs. skewed, `.skew()` and `.kurt()`, the **1.5 × IQR** fence rule (as a reusable function), z-scores and why they fail on skewed data, inspecting before deciding, log transforms, and capping with `.clip()`. |
| [04-Comparing_Groups.ipynb](04-Comparing_Groups.ipynb) | Group summaries with size + center + spread, **rates not counts**, `pd.crosstab()` with `normalize=`, `pivot_table()`, groups from `pd.cut()`, and two traps: tiny groups and **confounders**. |
| [05-Relationships_and_Correlation.ipynb](05-Relationships_and_Correlation.ipynb) | Covariance vs. correlation, `.corr()` for a pair or a matrix, listing the strongest pairs, **Pearson vs. Spearman**, why r ≈ 0 doesn't mean "no relationship," correlation vs. causation, and **Anscombe's quartet**. |
| [06-Describing_Data_Lab.ipynb](06-Describing_Data_Lab.ipynb) | Capstone lab: describe the Palmer Penguins dataset from raw file to saved report: clean, data dictionary, summaries, outliers overall vs. within species, species comparisons, and a **Simpson's paradox** in the bill measurements. Saves to `06-OutputFiles`. |

Each notebook ends with a **🏋️ Practice** section and an optional **🔥 Challenge**.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- Separate a column's **dtype** (storage) from its **measurement scale** (meaning), and say which statistics each scale allows
- Record meaning in pandas with `category`, ordered categories, and `bool`, and document a dataset with a data dictionary
- Compute and interpret center (mean, median, mode), spread (range, std, IQR, percentiles), and shape (skew, kurtosis)
- Choose robust statistics (median, IQR) for skewed data, and explain `ddof`
- Flag outliers with the IQR rule and z-scores, and decide whether to keep, fix, cap, or transform them
- Compare groups with sizes, rates, crosstabs, and pivot tables, and spot small groups and confounders
- Compute and interpret Pearson and Spearman correlation, and explain why correlation isn't causation
- Explain why summary statistics alone can hide important structure (Anscombe, Simpson's paradox)

---

## 🎯 Key Takeaways

> **The core habit:** ask what a column *means* before you summarize it, and never trust a single number on its own.

- **Storage isn't meaning.** IDs, class codes, and 0/1 outcomes are stored as numbers but aren't quantities.
- **Pair your statistics.** Median with IQR, mean with std, and every group statistic with its group size.
- **Outliers are unusual, not wrong.** Inspect them before you act, and remember that "unusual" depends on the comparison group.
- **Compare rates, not counts,** whenever the groups are different sizes.
- **Correlation measures straight-line association,** not causation, and not every kind of relationship.
- **Numbers compress data, and compression hides things.** That's why Module 08 exists.

---

## 🛠️ Tips

- Keep `iqr_fences()` (notebook 03) handy. You'll reuse it in the lab and in Module 08.
- When a group comparison surprises you, ask "what else differs between these groups?" before you believe it.
- Round for **display** (`.round(2)`), not before you compute.

---

## 📚 Also in this module

- [glossary.md](glossary.md) — key terms
- [quiz.md](quiz.md) — 36-question self-check with an answer key
- [worksheet.md](worksheet.md) — practice problems and reflection prompts

## ⬅️ Previously: [Module 06: Working with Data](../06-Working_with_Data_Adv/README.md)

## 🎨 Up Next: [Module 08: Visualizing Data](../08-Visualizing_Data/README.md)

You've described the data in numbers. Next, you'll **show** it: object-oriented Matplotlib, pandas plotting, and Seaborn, starting with the four Anscombe datasets that looked identical in notebook 05.
