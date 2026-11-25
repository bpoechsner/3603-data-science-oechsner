# 📝 Worksheet: 08 - Visualizing Data

Use this worksheet to reinforce object-oriented Matplotlib, pandas plotting, Seaborn, and chart design. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🖼️ Section 1: Matplotlib, Object-Oriented

1. What's the difference between `plt.title('X')` and `ax.set_title('X')`? When does the difference matter?  
   `Answer:` plt.title() titles whatever chart is current. ax.set_title() titles that exact chart. It matters when a figure has more than one chart.

2. You're comparing three histograms in a 1 × 3 figure. Name two settings that make the panels fair to compare.  
   `Answer:` sharey=True and the same bins in every panel.

---

### ✏️ Task: A Reusable Chart Function

```python
# Write plot_distribution(ax, series, title, unit) that draws a histogram on ax,
# marks the mean and median with vertical lines, and labels everything.
# Use it to build a 2 x 2 figure of Titanic Age, Fare (log scale!), SibSp, and Parch.
# Save the figure with fig.savefig().

titanic = pd.read_csv('titanic.csv')
OUT = Path('worksheet-OutputFiles')
OUT.mkdir(exist_ok=True)


def plot_distribution(ax, series, title, unit, bins=25):
    """Histogram of a numeric Series on ax, with its mean and median marked."""
    values = series.dropna()
    ax.hist(values, bins=bins, color='lightgray', edgecolor='white')
    ax.axvline(values.mean(), color='tab:red', linestyle='--', label=f'mean {values.mean():.1f}')
    ax.axvline(values.median(), color='tab:blue', label=f'median {values.median():.1f}')
    ax.set(title=title, xlabel=unit, ylabel='Passengers')
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(frameon=False)


fare = titanic['Fare']
paid = fare[fare > 0]

fig, axes = plt.subplots(2, 2, figsize=(11, 8), layout='constrained')
ax1, ax2, ax3, ax4 = axes.flat

plot_distribution(ax1, titanic['Age'], 'Age', 'years')
plot_distribution(ax2, paid, 'Fare (excludes £0 fares)', '£ (log scale)',
                  bins=np.geomspace(paid.min(), paid.max(), 30))
ax2.set_xscale('log')
plot_distribution(ax3, titanic['SibSp'], 'Siblings/Spouses Aboard', 'count', bins=range(0, 10))
plot_distribution(ax4, titanic['Parch'], 'Parents/Children Aboard', 'count', bins=range(0, 8))

fig.suptitle('Titanic Passenger Distributions')
fig.savefig(OUT / 'titanic_distributions.png', dpi=150, bbox_inches='tight')
plt.show()

```

### 🤖 Explain It

In your own words: why is a function that takes an `ax` argument more useful than a function that calls `plt.` directly?

A function that takes an ax can draw on any panel. One that uses plt only draws on the current chart.

---

## 🐼 Section 2: Plotting with Pandas

3. When you call `.plot.bar()` on a DataFrame, what does the index become, and what do the columns become?  
   `Answer:` The index becomes the x-axis categories, and each column becomes its own set of bars.

4. Give one example of wide data and the same data in long form.  
   `Answer:` Wide: one row per class, with female and male columns. Long: one row per class and sex pair, with columns class, Sex and rate.

---

### ✏️ Task: Summary Table to Chart

```python
# Using pokemon.csv:
# 1. Build a crosstab of Generation vs. Legendary, normalized by row.
# 2. Plot it as a 100% stacked bar chart with a percent-formatted axis.
# 3. Melt the (un-normalized) crosstab into long form with columns Generation, Legendary, count.

poke = pd.read_csv('pokemon.csv')

legendary = pd.crosstab(poke['Generation'], poke['Legendary'], normalize='index')

ax = legendary.plot.bar(stacked=True, rot=0, figsize=(8, 4))
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
ax.set(title='Legendary Share by Generation', xlabel='Generation', ylabel='Share of Pokémon')
ax.legend(title='Legendary', bbox_to_anchor=(1.01, 1), loc='upper left')
plt.show()

counts = pd.crosstab(poke['Generation'], poke['Legendary'])
long = counts.reset_index().melt(id_vars='Generation', var_name='Legendary', value_name='count')
print(long)

```

### 🤖 Explain It

In your own words: when would you plot with pandas `.plot`, and when would you switch to Seaborn?

Pandas .plot for quick charts of a summary table. Seaborn for raw data, hue/col grouping, distributions or error bars.

---

## 🌊 Section 3: Seaborn Distributions

5. Why can a histogram with `hue` and raw counts be misleading when the groups are very different sizes? What's the fix?  
   `Answer:` The bigger group's bars hide the smaller group. Fix: stat='percent' with common_norm=False.

6. Explain how a box plot's whiskers and dots connect to the 1.5 × IQR rule from Module 07.  
   `Answer:` The box is Q1 to Q3. The whiskers reach the last points inside the 1.5 × IQR fences, and the dots are the outliers past them.

---

### ✏️ Task: Compare Distributions Four Ways

```python
# Using penguins.csv, for flipper_length_mm by species, make a 2 x 2 figure:
# a step histogram with hue, a KDE with hue, a box plot, and a violin plot.
# Use the same species order and the same colors in every panel.

sns.set_theme(style='whitegrid')
MEASUREMENTS = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
penguins = pd.read_csv('penguins.csv').dropna(subset=MEASUREMENTS)
SPECIES = ['Adelie', 'Chinstrap', 'Gentoo']
SPECIES_COLORS = dict(zip(SPECIES, sns.color_palette('colorblind', 3)))

fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout='constrained')
ax1, ax2, ax3, ax4 = axes.flat

sns.histplot(data=penguins, x='flipper_length_mm', hue='species', hue_order=SPECIES,
             palette=SPECIES_COLORS, element='step', ax=ax1)
ax1.set(title='Step histogram', xlabel='Flipper length (mm)')

sns.kdeplot(data=penguins, x='flipper_length_mm', hue='species', hue_order=SPECIES,
            palette=SPECIES_COLORS, fill=True, alpha=0.3, common_norm=False, ax=ax2)
ax2.set(title='KDE', xlabel='Flipper length (mm)')

sns.boxplot(data=penguins, x='species', y='flipper_length_mm', order=SPECIES,
            hue='species', palette=SPECIES_COLORS, legend=False, ax=ax3)
ax3.set(title='Box plot', xlabel='', ylabel='Flipper length (mm)')

sns.violinplot(data=penguins, x='species', y='flipper_length_mm', order=SPECIES,
               hue='species', palette=SPECIES_COLORS, legend=False, inner='quart', ax=ax4)
ax4.set(title='Violin plot', xlabel='', ylabel='Flipper length (mm)')

fig.suptitle('Flipper Length by Species, Four Ways')
plt.show()

```

### 🤖 Explain It

In your own words: the overall penguin body-mass histogram looked like one lumpy pile, and its skew was only 0.47. What did coloring by species reveal, and why couldn't the skew statistic reveal it?

Gentoos were a separate, heavier group. Skew only measures lopsidedness, and two humps side by side can still look symmetric.

---

## 🔍 Section 4: Seaborn Relationships and Categories

7. What do the error bars on a default `sns.barplot()` mean? How would `errorbar='sd'` change them?  
   `Answer:` A 95% confidence interval for the mean. errorbar='sd' shows the spread of individual values instead, so the bars get longer.

8. Why should you color a scatter plot by group before adding a trend line?  
   `Answer:` Groups can have different trends, and one line through all of them can show the opposite trend.

---

### ✏️ Task: Reveal the Paradox

```python
# Using penguins.csv:
# 1. Draw one regplot of bill_length_mm vs. bill_depth_mm for all penguins.
# 2. Draw one regplot per species on a second panel, with r in each label.
# 3. Give each panel a title that states what it shows.

fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharex=True, sharey=True, layout='constrained')

r_all = penguins['bill_length_mm'].corr(penguins['bill_depth_mm'])
sns.regplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', ax=axes[0],
            scatter_kws={'alpha': 0.4, 'color': 'gray'}, line_kws={'color': 'black'})
axes[0].set(title=f'All Penguins: Longer Bills Look Shallower (r = {r_all:.2f})')

for species, group in penguins.groupby('species'):
    r = group['bill_length_mm'].corr(group['bill_depth_mm'])
    sns.regplot(data=group, x='bill_length_mm', y='bill_depth_mm', ax=axes[1],
                color=SPECIES_COLORS[species], scatter_kws={'alpha': 0.5}, label=f'{species} (r = {r:.2f})')
axes[1].set(title='Within Every Species, Longer Bills Are Deeper')
axes[1].legend()

for ax in axes:
    ax.set(xlabel='Bill length (mm)', ylabel='Bill depth (mm)')

plt.show()
```

### 🤖 Explain It

In your own words: explain Simpson's paradox to someone who has never heard of it, using your chart from the task above.

All penguins together, longer bills look shallower (r = −0.24). Within each species, longer bills are deeper. Gentoos have long, shallow bills, which drags the combined line down.

---

## 🗣️ Section 5: Choosing and Telling

9. Name three things a bar chart's y-axis can do to mislead a reader.  
   `Answer:` Not starting at zero, different scales on compared panels, and an axis range too large that flattens the differences.

10. What's the difference between a descriptive title and a finding title? Write one of each for the same chart.  
    `Answer:` A descriptive title says what's plotted, and a finding title says what it shows. "Survival Rate by Class" vs. "1st Class Passengers Were Most Likely to Survive".

---

### ✏️ Task: Makeover

```python
# Start with: titanic.groupby('Embarked')['Fare'].mean().plot.bar()
# Redesign it with the notebook 05 checklist: the right statistic for skewed data,
# readable port names, sorted bars, a highlight color, bar labels, and a finding title.
# Save the before and after versions.

ax = titanic.groupby('Embarked')['Fare'].mean().plot.bar()
plt.savefig(OUT / 'worksheet_makeover_before.png', dpi=120, bbox_inches='tight')
plt.show()

titanic['port'] = titanic['Embarked'].map({'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'})
port_fare = titanic.groupby('port')['Fare'].median().sort_values()
colors = ['tab:orange' if p == 'Cherbourg' else 'lightgray' for p in port_fare.index]

fig, ax = plt.subplots(figsize=(8, 3.5))
port_fare.plot.barh(ax=ax, color=colors)
ax.bar_label(ax.containers[0], labels=[f'£{v:.2f}' for v in port_fare], padding=3)
ax.set(xlim=(0, 35), xlabel='Median fare (£)', ylabel='')
ax.set_title('Cherbourg Passengers Paid More Than Twice What Others Paid', loc='left', fontweight='bold', pad=24)
ax.text(0, 1.03, 'Median Titanic fare by port of embarkation (889 passengers)',
        transform=ax.transAxes, color='gray')
ax.spines[['top', 'right']].set_visible(False)
fig.savefig(OUT / 'worksheet_makeover_after.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 🤖 Explain It

In your own words: what's the difference between a chart made for exploration and a chart made for communication? Why do they need different amounts of polish?

Exploration charts are quick ones for me. Communication charts are for someone else, so they need a finding title, labels and honest scales.

---

## 🧾 Submit Checklist

- [ ] I built a multi-panel Matplotlib figure with `fig, ax`, shared axes, and `fig.savefig()`.
- [ ] I used a log scale, a reference line, and a tick formatter where they helped.
- [ ] I turned a pandas summary table into a chart, and reshaped data between wide and long.
- [ ] I compared distributions across groups fairly (`common_norm=False`, shared axes, sample sizes).
- [ ] I showed a relationship with a scatter plot colored by group, and explained my error bars.
- [ ] I redesigned a default chart using the checklist, with a finding title.
- [ ] I completed the "Explain It" prompts in my own words.
