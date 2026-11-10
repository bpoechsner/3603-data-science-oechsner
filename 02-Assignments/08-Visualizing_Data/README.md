# 🎨 Module 08: Visualizing Data

Module 07 ended with four datasets that had identical statistics and looked nothing alike. This module is about **looking**. You'll start where Foundations 07 left off (basic `plt.` charts) and build up to object-oriented Matplotlib, one-line pandas plots, Seaborn's statistical charts, and the judgment to choose, design, and title a chart so it tells the truth clearly.

The module ends where Module 07 did: with the Palmer Penguins, turning your numeric report into a set of figures.

All notebooks use **local data files in this folder** (`titanic.csv`, `pokemon.csv`, `penguins.csv`, and `anscombe.csv`), so nothing downloads over the network. Every notebook saves its charts to its own `NN-OutputFiles` folder.

---

## 🗂 Notebook Overview

| Notebook | Description |
|----------|-------------|
| [01-Matplotlib_Object_Oriented.ipynb](01-Matplotlib_Object_Oriented.ipynb) | Opens by plotting **Anscombe's quartet**. Then: pyplot vs. `fig, ax`, `ax.set()`, reference lines for Module 07 statistics, **log scales** for skewed data, money/percent tick formatters, `annotate`, `bar_label`, decluttering, multi-panel figures with `sharey` and `layout='constrained'`, `savefig`/`close`, and functions that draw on an `ax`. |
| [02-Plotting_with_Pandas.ipynb](02-Plotting_with_Pandas.ipynb) | `.plot.<kind>()` on Series and DataFrames; turning `value_counts`, `groupby`, `crosstab`, and `pivot_table` straight into charts; sorted vs. ordered bars; grouped and **100% stacked** bars; `ax=` for panels; and **wide vs. long** data with `.melt()`, the bridge to Seaborn. |
| [03-Seaborn_Distributions.ipynb](03-Seaborn_Distributions.ipynb) | Seaborn's column-mapping model, **axes-level vs. figure-level**, `histplot` (`binwidth`, `hue`, `multiple=`, `stat=`, `common_norm=False`), KDE and ECDF plots, the **box plot as the IQR fence rule**, violin and strip plots, and small multiples with `displot(col=, row=)`. |
| [04-Seaborn_Relationships_and_Categories.ipynb](04-Seaborn_Relationships_and_Categories.ipynb) | Scatter plots with `hue`/`style`, overplotting, `regplot`/`lmplot`, the **penguin Simpson's paradox** made visible, Anscombe's identical fitted lines, `countplot` vs. `barplot` vs. `pointplot`, **what error bars mean**, diverging vs. sequential heatmaps, and `pairplot`. |
| [05-Choosing_and_Telling.ipynb](05-Choosing_and_Telling.ipynb) | Choosing a chart from the question and the data types, **honest scales**, ordering categories, color that highlights (colorblind-safe, consistent), **finding titles** and direct labels, a step-by-step **makeover**, and a final checklist. |
| [06-Visualization_Lab.ipynb](06-Visualization_Lab.ipynb) | Capstone lab: turn the Module 07 penguin report into a consistent, titled figure set (distributions, species × sex, island composition, correlations), then build the **paradox figure** and a **one-page summary** yourself. Saves to `06-OutputFiles`. |

Each notebook ends with a **🏋️ Practice** section and an optional **🔥 Challenge**.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- Build charts with Matplotlib's object-oriented interface (`fig`, `ax`), including multi-panel figures, and save them
- Mark statistics on charts, use log scales for skewed data, and format ticks as money or percentages
- Turn pandas summary tables into charts with `.plot`, and reshape between wide and long data
- Use Seaborn to compare distributions across groups (`histplot`, `kdeplot`, `ecdfplot`, `boxplot`, `violinplot`, `stripplot`, `displot`)
- Use Seaborn to show relationships and group estimates (`scatterplot`, `regplot`/`lmplot`, `barplot`, `pointplot`, `heatmap`, `pairplot`), and explain what their error bars mean
- Choose a chart from the question and the column types, and keep its scales, order, and colors honest
- Write titles that state findings, label data directly, and redesign a default chart for an audience
- Explain how a chart can reveal what summary statistics hide (Anscombe, Simpson's paradox, mixed groups)

---

## 🎯 Key Takeaways

> **The core habit:** plot first, then summarize, and check every chart against the numbers.

- **`fig` is the canvas and `ax` is one chart.** Call methods on the object you mean.
- **Pandas plots wide data, and Seaborn plots long data.** `.melt()` and `pivot_table` move between them.
- **Compare groups fairly in charts too:** shared axes, `common_norm=False`, sample sizes in labels.
- **A box plot is the IQR rule.** Violins show shape, and strips show every point.
- **Color by group before you fit a line.** One chart can reveal Simpson's paradox.
- **Bars start at zero, and colors mean something.** Titles say what the chart shows.

---

## 🛠️ Tips

- Define your palette dictionary and category order **once**, at the top of a notebook, and pass them to every chart.
- Call `fig.savefig()` **before** `plt.show()`.
- When a chart looks surprising, go back to the numbers (Module 07) before you believe it, and the other way around.

---

## 📚 Also in this module

- [glossary.md](glossary.md) — key terms
- [quiz.md](quiz.md) — 36-question self-check with an answer key
- [worksheet.md](worksheet.md) — practice problems and reflection prompts

## ⬅️ Previously: [Module 07: Describing Data](../07-Describing_Data/README.md)

## 🏁 Up Next: the Final Project

Take a dataset of your own through the whole cycle: load, clean (06), describe (07), visualize (08), and explain what you found.
