# 📝 Worksheet: 08 - Visualizing Data

Use this worksheet to reinforce object-oriented Matplotlib, pandas plotting, Seaborn, and chart design. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🖼️ Section 1: Matplotlib, Object-Oriented

1. What's the difference between `plt.title('X')` and `ax.set_title('X')`? When does the difference matter?  
   `Answer:` _______________________

2. You're comparing three histograms in a 1 × 3 figure. Name two settings that make the panels fair to compare.  
   `Answer:` _______________________

---

### ✏️ Task: A Reusable Chart Function

```python
# Write plot_distribution(ax, series, title, unit) that draws a histogram on ax,
# marks the mean and median with vertical lines, and labels everything.
# Use it to build a 2 x 2 figure of Titanic Age, Fare (log scale!), SibSp, and Parch.
# Save the figure with fig.savefig().
```

### 🤖 Explain It

In your own words: why is a function that takes an `ax` argument more useful than a function that calls `plt.` directly?

---

## 🐼 Section 2: Plotting with Pandas

3. When you call `.plot.bar()` on a DataFrame, what does the index become, and what do the columns become?  
   `Answer:` _______________________

4. Give one example of wide data and the same data in long form.  
   `Answer:` _______________________

---

### ✏️ Task: Summary Table to Chart

```python
# Using pokemon.csv:
# 1. Build a crosstab of Generation vs. Legendary, normalized by row.
# 2. Plot it as a 100% stacked bar chart with a percent-formatted axis.
# 3. Melt the (un-normalized) crosstab into long form with columns Generation, Legendary, count.
```

### 🤖 Explain It

In your own words: when would you plot with pandas `.plot`, and when would you switch to Seaborn?

---

## 🌊 Section 3: Seaborn Distributions

5. Why can a histogram with `hue` and raw counts be misleading when the groups are very different sizes? What's the fix?  
   `Answer:` _______________________

6. Explain how a box plot's whiskers and dots connect to the 1.5 × IQR rule from Module 07.  
   `Answer:` _______________________

---

### ✏️ Task: Compare Distributions Four Ways

```python
# Using penguins.csv, for flipper_length_mm by species, make a 2 x 2 figure:
# a step histogram with hue, a KDE with hue, a box plot, and a violin plot.
# Use the same species order and the same colors in every panel.
```

### 🤖 Explain It

In your own words: the overall penguin body-mass histogram looked like one lumpy pile, and its skew was only 0.47. What did coloring by species reveal, and why couldn't the skew statistic reveal it?

---

## 🔍 Section 4: Seaborn Relationships and Categories

7. What do the error bars on a default `sns.barplot()` mean? How would `errorbar='sd'` change them?  
   `Answer:` _______________________

8. Why should you color a scatter plot by group before adding a trend line?  
   `Answer:` _______________________

---

### ✏️ Task: Reveal the Paradox

```python
# Using penguins.csv:
# 1. Draw one regplot of bill_length_mm vs. bill_depth_mm for all penguins.
# 2. Draw one regplot per species on a second panel, with r in each label.
# 3. Give each panel a title that states what it shows.
```

### 🤖 Explain It

In your own words: explain Simpson's paradox to someone who has never heard of it, using your chart from the task above.

---

## 🗣️ Section 5: Choosing and Telling

9. Name three things a bar chart's y-axis can do to mislead a reader.  
   `Answer:` _______________________

10. What's the difference between a descriptive title and a finding title? Write one of each for the same chart.  
    `Answer:` _______________________

---

### ✏️ Task: Makeover

```python
# Start with: titanic.groupby('Embarked')['Fare'].mean().plot.bar()
# Redesign it with the notebook 05 checklist: the right statistic for skewed data,
# readable port names, sorted bars, a highlight color, bar labels, and a finding title.
# Save the before and after versions.
```

### 🤖 Explain It

In your own words: what's the difference between a chart made for exploration and a chart made for communication? Why do they need different amounts of polish?

---

## 🧾 Submit Checklist

- [ ] I built a multi-panel Matplotlib figure with `fig, ax`, shared axes, and `fig.savefig()`.
- [ ] I used a log scale, a reference line, and a tick formatter where they helped.
- [ ] I turned a pandas summary table into a chart, and reshaped data between wide and long.
- [ ] I compared distributions across groups fairly (`common_norm=False`, shared axes, sample sizes).
- [ ] I showed a relationship with a scatter plot colored by group, and explained my error bars.
- [ ] I redesigned a default chart using the checklist, with a finding title.
- [ ] I completed the "Explain It" prompts in my own words.
