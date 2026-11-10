# 📝 Worksheet: 07 - Describing Data

Use this worksheet to reinforce the descriptive workflow: what each column means, what's typical, how much it varies, what's unusual, how groups differ, and which columns move together. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🏷️ Section 1: Types of Data

1. Classify each as nominal, ordinal, interval, or ratio: `zip code`, `t-shirt size (S/M/L/XL)`, `year of birth`, `monthly rent`.  
   `Answer:` _______________________

2. A column has dtype `int64` and only 4 distinct values. Name two things it might really be, and how you'd decide.  
   `Answer:` _______________________

---

### ✏️ Task: Record the Meaning

```python
# Using titanic.csv:
# 1. Convert Embarked to 'category' and map C/Q/S to 'Cherbourg'/'Queenstown'/'Southampton'.
# 2. Create an ordered 'class' column (3rd < 2nd < 1st).
# 3. Print the share of passengers above 3rd class, using a comparison on 'class'.
```

### 🤖 Explain It

In your own words: why does it matter whether a variable is nominal or ordinal before you compute anything with it? What could go wrong if you averaged an ordinal column's codes?

---

## 🎯 Section 2: Center and Spread

3. Why is the median usually reported for house prices instead of the mean?  
   `Answer:` _______________________

4. You compute a standard deviation with pandas and get 14.53, and a classmate uses NumPy and gets 14.52. Who's wrong?  
   `Answer:` _______________________

---

### ✏️ Task: Compare Center and Spread

```python
# Using pokemon.csv:
# For Attack, print the mean, median, std, and IQR.
# Then do the same for Legendary Pokémon only.
# Which group is more spread out, by std and by IQR? Do the two measures agree?
```

### 🤖 Explain It

In your own words: two classes have the same average exam score, but very different standard deviations. Describe what being a student in each class might be like.

---

## 📐 Section 3: Shape and Outliers

5. A column has mean 50, median 38, and `.skew()` of 2.1. Describe its shape.  
   `Answer:` _______________________

6. Name one situation where you **should** remove an outlier, and one where you shouldn't.  
   `Answer:` _______________________

---

### ✏️ Task: Outlier Report

```python
# Using penguins.csv (drop the 2 rows with no measurements first):
# 1. Write or copy iqr_fences(series, k=1.5).
# 2. Count outliers in body_mass_g overall, then within each species.
# 3. Print the flagged rows. Are any of them impossible values?
```

### 🤖 Explain It

In your own words: explain to a classmate why "outlier" and "error" aren't the same thing, using an example from the Titanic fares.

---

## 👥 Section 4: Comparing Groups

7. When should you compare groups with counts, and when with rates?  
   `Answer:` _______________________

8. What's the difference between `normalize='index'` and `normalize='columns'` in `pd.crosstab()`? Write a question each one answers.  
   `Answer:` _______________________

---

### ✏️ Task: Survival Table

```python
# Using titanic.csv:
# 1. Bin Age into child (0-12), teen (13-18), adult (19-60), senior (61+) with pd.cut().
# 2. Build a pivot_table of survival rate with age group as rows and Sex as columns.
# 3. Add the group sizes (a second pivot_table with aggfunc='size').
# Which cell has the highest rate? Is its group big enough to trust?
```

### 🤖 Explain It

In your own words: what's a confounder? Describe one in the Titanic data, and how you'd check for it with a table.

---

## 🔗 Section 5: Relationships and Correlation

9. When would you use Spearman instead of Pearson?  
   `Answer:` _______________________

10. A news story says "cities with more ice-cream sales have more drownings." Give a likely confounder.  
    `Answer:` _______________________

---

### ✏️ Task: Correlation Report

```python
# Using pokemon.csv:
# 1. Compute the Pearson and Spearman correlation matrices of the six stats.
# 2. List the three strongest pairs (use the upper triangle).
# 3. Recompute r(Attack, Defense) for Legendary and non-Legendary separately.
```

### 🤖 Explain It

In your own words: Anscombe's four datasets all have r = 0.82. What does that teach you about reporting a correlation without a plot? What's the danger of a single summary number?

---

## 🧾 Submit Checklist

- [ ] I built a data dictionary that separates dtype from measurement scale.
- [ ] I used an ordered category and computed a proportion from a boolean column.
- [ ] I reported center and spread that fit a column's shape, and explained `ddof`.
- [ ] I flagged outliers with the IQR rule, inspected them, and decided what to do with them.
- [ ] I compared groups with sizes and rates, using a crosstab and a pivot table.
- [ ] I computed Pearson and Spearman correlations and explained a possible confounder.
- [ ] I completed the "Explain It" prompts in my own words.
