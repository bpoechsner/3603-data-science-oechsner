# 📝 Worksheet: 07 - Describing Data

Use this worksheet to reinforce the descriptive workflow: what each column means, what's typical, how much it varies, what's unusual, how groups differ, and which columns move together. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🏷️ Section 1: Types of Data

1. Classify each as nominal, ordinal, interval, or ratio: `zip code`, `t-shirt size (S/M/L/XL)`, `year of birth`, `monthly rent`.  
   `Answer:` Zip code: nominal. T-shirt size: ordinal. Year of birth: interval. Monthly rent: ratio.

2. A column has dtype `int64` and only 4 distinct values. Name two things it might really be, and how you'd decide.  
   `Answer:` It could be a category code (like Pclass 1/2/3, or a 0/1/2/3 rating) or a real small count (like SibSp). Decide by what the column measures: ask whether 2.5 of it, or “twice as much,” makes sense.

---

### ✏️ Task: Record the Meaning

```python
# Using titanic.csv:
# 1. Convert Embarked to 'category' and map C/Q/S to 'Cherbourg'/'Queenstown'/'Southampton'.
# 2. Create an ordered 'class' column (3rd < 2nd < 1st).
# 3. Print the share of passengers above 3rd class, using a comparison on 'class'.

titanic = pd.read_csv('titanic.csv')

port_names = {'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'}
titanic['Embarked'] = titanic['Embarked'].map(port_names).astype('category')
print(titanic['Embarked'].cat.categories)

class_labels = {1: '1st', 2: '2nd', 3: '3rd'}
class_order = pd.CategoricalDtype(['3rd', '2nd', '1st'], ordered=True)
titanic['class'] = titanic['Pclass'].map(class_labels).astype(class_order)

print(f"Share above 3rd class: {(titanic['class'] > '3rd').mean():.1%}")
```

### 🤖 Explain It

In your own words: why does it matter whether a variable is nominal or ordinal before you compute anything with it? What could go wrong if you averaged an ordinal column's codes?

Nominal categories have no order, so only counts and the mode make sense. Ordinal categories have an order but unequal gaps. Averaging class codes (2.31) treats 1st→2nd and 2nd→3rd as equal steps, which isn’t true.

---

## 🎯 Section 2: Center and Spread

3. Why is the median usually reported for house prices instead of the mean?  
   `Answer:` A few very expensive houses pull the mean up. The median shows what a typical house costs.

4. You compute a standard deviation with pandas and get 14.53, and a classmate uses NumPy and gets 14.52. Who's wrong?  
   `Answer:` Neither. Pandas divides by n − 1 (ddof=1, for a sample) and NumPy divides by n (ddof=0, for a population).

---

### ✏️ Task: Compare Center and Spread

```python
# Using pokemon.csv:
# For Attack, print the mean, median, std, and IQR.
# Then do the same for Legendary Pokémon only.
# Which group is more spread out, by std and by IQR? Do the two measures agree? All Pokemon are more spread out by both std (32.46 vs 30.35) and IQR (45 vs 31). They agree

poke = pd.read_csv('pokemon.csv')

groups = {'All': poke['Attack'], 'Legendary': poke[poke['Legendary']]['Attack']}
for name, attack in groups.items():
    q1 = attack.quantile(0.25)
    q3 = attack.quantile(0.75)
    print(f'{name:10} mean: {attack.mean():.2f}   median: {attack.median():.2f}   std: {attack.std():.2f}   IQR: {q3 - q1:.2f}')
```

### 🤖 Explain It

In your own words: two classes have the same average exam score, but very different standard deviations. Describe what being a student in each class might be like.

Low std: most students score near the average, so the class moves at one pace. High std: some students are far ahead and some far behind, so the average describes almost nobody.
---

## 📐 Section 3: Shape and Outliers

5. A column has mean 50, median 38, and `.skew()` of 2.1. Describe its shape.  
   `Answer:` Strongly right-skewed: most values are low, with a long tail of large values pulling the mean above the median.

6. Name one situation where you **should** remove an outlier, and one where you shouldn't.  
   `Answer:` Remove one that’s impossible and can’t be fixed (age 250). Keep one that’s real but extreme (a £512 Titanic ticket).

---

### ✏️ Task: Outlier Report

```python
# Using penguins.csv (drop the 2 rows with no measurements first):
# 1. Write or copy iqr_fences(series, k=1.5).
# 2. Count outliers in body_mass_g overall, then within each species.
# 3. Print the flagged rows. Are any of them impossible values?

MEASUREMENTS = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
penguins = pd.read_csv('penguins.csv')
clean = penguins.dropna(subset=MEASUREMENTS).copy()


def iqr_fences(series, k=1.5):
    """Return the (lower, upper) outlier fences for a numeric Series."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


low, high = iqr_fences(clean['body_mass_g'])
mass_outlier = (clean['body_mass_g'] < low) | (clean['body_mass_g'] > high)
print(f'Overall fences: {low:.1f} to {high:.1f}   outliers: {mass_outlier.sum()}')

flagged = []
for species, group in clean.groupby('species'):
    low, high = iqr_fences(group['body_mass_g'])
    in_species = (group['body_mass_g'] < low) | (group['body_mass_g'] > high)
    print(f'{species:<10} fences {low:7.1f} to {high:7.1f}   outliers: {in_species.sum()}')
    flagged.append(group[in_species])

pd.concat(flagged)
# Two Chinstraps (2700 g and 4800 g). Both are possible penguin weights, so they're not errors.
```

### 🤖 Explain It

In your own words: explain to a classmate why "outlier" and "error" aren't the same thing, using an example from the Titanic fares.

An outlier is just unusual. An error is impossible or wrong. The £512 Titanic fares are outliers, but they’re real 1st-class tickets shared by groups, so deleting them would misrepresent what people paid.
---

## 👥 Section 4: Comparing Groups

7. When should you compare groups with counts, and when with rates?  
   `Answer:` Use counts when the groups are the same size or you need totals. Use rates when the group sizes differ.

8. What's the difference between `normalize='index'` and `normalize='columns'` in `pd.crosstab()`? Write a question each one answers.  
   `Answer:` 'index' makes each row add to 100% (“Within 1st class, what share is female?”). 'columns' makes each column add to 100% (“Of all women, what share was in 1st class?”).

---

### ✏️ Task: Survival Table

```python
# Using titanic.csv:
# 1. Bin Age into child (0-12), teen (13-18), adult (19-60), senior (61+) with pd.cut().
# 2. Build a pivot_table of survival rate with age group as rows and Sex as columns.
# 3. Add the group sizes (a second pivot_table with aggfunc='size').
# Which cell has the highest rate? Is its group big enough to trust?

titanic['age_group'] = pd.cut(
    titanic['Age'],
    bins=[0, 12, 18, 60, 100],
    labels=['child', 'teen', 'adult', 'senior'],
)

survival_rate = titanic.pivot_table(
    values='Survived', index='age_group', columns='Sex', aggfunc='mean', observed=True,
)
print((survival_rate * 100).round(1))

group_sizes = titanic.pivot_table(
    values='Survived', index='age_group', columns='Sex', aggfunc='size', observed=True,
)
group_sizes
# Highest: senior women at 100%, but that's only 3 people. Too small to trust.
```

### 🤖 Explain It

In your own words: what's a confounder? Describe one in the Titanic data, and how you'd check for it with a table.

A confounder is a hidden variable tied to both the group and the outcome. Cherbourg passengers survived more, but more of them were 1st class. Check with a crosstab of port vs. class, then compare survival by port within each class.

---

## 🔗 Section 5: Relationships and Correlation

9. When would you use Spearman instead of Pearson?  
   `Answer:` Use Spearman for ordinal data, curved but always-rising relationships, or data with outliers or heavy skew.

10. A news story says "cities with more ice-cream sales have more drownings." Give a likely confounder.  
    `Answer:` Hot weather: it raises both ice-cream sales and swimming.

---

### ✏️ Task: Correlation Report

```python
# Using pokemon.csv:
# 1. Compute the Pearson and Spearman correlation matrices of the six stats.
# 2. List the three strongest pairs (use the upper triangle).
# 3. Recompute r(Attack, Defense) for Legendary and non-Legendary separately.

stats = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

pearson = poke[stats].corr()
spearman = poke[stats].corr(method='spearman')

mask = np.triu(np.ones(pearson.shape, dtype=bool), k=1)
print(pearson.where(mask).stack().dropna().rename('r').sort_values(key=abs, ascending=False).round(3).head(3))
print(spearman.where(mask).stack().dropna().rename('rho').sort_values(key=abs, ascending=False).round(3).head(3))

poke.groupby('Legendary').apply(lambda d: d['Attack'].corr(d['Defense'])).round(3)
```

### 🤖 Explain It

In your own words: Anscombe's four datasets all have r = 0.82. What does that teach you about reporting a correlation without a plot? What's the danger of a single summary number?

Four very different datasets (a line, a curve, a line with one outlier, a vertical stack) share r = 0.82. A single number can’t show shape or outliers, so a correlation without a plot can describe a pattern that isn’t there.
---

## 🧾 Submit Checklist

- [ ] I built a data dictionary that separates dtype from measurement scale.
- [ ] I used an ordered category and computed a proportion from a boolean column.
- [ ] I reported center and spread that fit a column's shape, and explained `ddof`.
- [ ] I flagged outliers with the IQR rule, inspected them, and decided what to do with them.
- [ ] I compared groups with sizes and rates, using a crosstab and a pivot table.
- [ ] I computed Pearson and Spearman correlations and explained a possible confounder.
- [ ] I completed the "Explain It" prompts in my own words.
