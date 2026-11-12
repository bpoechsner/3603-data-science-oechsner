# 📝 Worksheet: 06 - Working with Data (Advanced)

Use this worksheet to reinforce Pandas Series/DataFrames and the core data-wrangling workflow: load, explore, select, clean, transform, sort/filter/search, group, and combine. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🐼 Section 1: Series and DataFrames

1. What's the difference between a Pandas `Series` and a `DataFrame`? How does a list of dictionaries (from Module 03) turn into one?  
   `Answer:` A Series is one labeled column of values. A DataFrame is a table of rows and columns, where each column is a Series. With a list of dictionaries, each dictionary becomes a row and the keys become the column names.

2. If you add two `Series` together and a label appears in only one of them, what value do you get at that label, and why?  
   `Answer:` NaN. Pandas lines up values by label, so a label in only one Series has nothing to add to.

---

### ✏️ Task: Series Basics

```python
# Create a Series from a dictionary mapping 4 of your classes to your grade in each.
# Print the Series, then print the average of all grades (hint: .mean()).

grades = pd.Series({'Circuits II': 92, 'Signals': 88, 'Data Science': 95, 'Electronics': 90})
print(grades)
print('Average grade:', grades.mean())
```



### 🤖 Explain It

In your own words: how is a Pandas `Series` similar to a Python dictionary, and how is it similar to a list? What does it borrow from each?

A Series is like a dictionary because each value has a label you can look it up by. It’s like a list because the values are kept in order and you can do math or filtering on all of them at once.

---

## 📂 Section 2: Loading and Exploring

3. What does `df.info()` tell you that `df.describe()` doesn't?  
   `Answer:` .info() shows the dtypes and non-null counts for every column. .describe() shows summary statistics and, by default, only for numeric columns.

4. If `df.isnull().sum()` shows `Age: 177`, what does that number mean?  
   `Answer:` 177 rows have no value recorded for Age.

5. In `titanic.csv`, what does **one row** represent, and which column identifies each row?  
   `Answer:` One row represents one passenger. PassengerId identifies each row.

---

### ✏️ Task: First Look at a Dataset

```python
# Load pokemon.csv.
# Print its shape, its columns, and .describe() for just the numeric columns.
# Which column has the most missing values, if any?

poke = pd.read_csv('pokemon.csv')
print('Shape:', poke.shape)
print('Columns:', poke.columns.tolist())
print(poke.describe())
print(poke.isnull().sum())

# Type 2 has the most missing values
```



### 🤖 Explain It

In your own words: why is it worth running `.info()` and `.isnull().sum()` on a dataset *before* you start analyzing it, rather than jumping straight to the questions you actually care about?

It shows you what you’re actually working with before you trust any results. Missing values, wrong types, and duplicates can quietly break averages and filters if you don’t catch them first.

---

## 🎯 Section 3: Indexing and Selection

6. Rewrite this using `.loc[]` instead of bracket + `.iloc[]` mixed together — or explain why you can't mix them the way it's written:
```python
df.iloc[df['Age'] < 10]  # this is actually broken — why?
```
   `Answer:` .iloc[] only takes positions. A True/False mask has to go through .loc[] or plain brackets. Fix: df.loc[df['Age'] < 10]

7. What's wrong with `df[df['Age'] < 10 and df['Fare'] > 100]`, and how would you fix it?  
   `Answer:` Python’s and can’t compare a whole column of True/False values at once, so it raises a ValueError. Use & with each condition in parentheses: df[(df['Age'] < 10) & (df['Fare'] > 100)]

8. Rewrite `df[(df['Pclass'] == 1) | (df['Pclass'] == 2)]` with `.isin()`. Why is `.isin()` easier to read when there are five values to match instead of two?  
   `Answer:` df[df['Pclass'].isin([1, 2])]. With five values, .isin() is one short list instead of five conditions joined with |.

---

### ✏️ Task: Titanic Slicing

```python
# Using titanic.csv:
# 1. Select passengers in 3rd class (Pclass == 3) who survived (Survived == 1).
# 2. Of those, show only the Name, Age, and Fare columns.
# 3. Sort the result by Fare, descending.

titanic = pd.read_csv('titanic.csv')
(titanic.loc[(titanic['Pclass'] == 3) & (titanic['Survived'] == 1), ['Name', 'Age', 'Fare']]
   .sort_values('Fare', ascending=False))
```

### 🤖 Explain It

In your own words: why does `df.iloc[df['Age'] < 10]` not work, when `df.loc[df['Age'] < 10]` and `df[df['Age'] < 10]` both do?

.iloc[] only understands row positions like 0, 1 and 2. A mask is a column of True/False values, which is a condition, not a position. .loc[] and plain brackets are built to take a mask and keep the True rows.

---

## 🧼 Section 4: Cleaning

9. If a column has the values `['25', 'thirty', '35']`, what happens when you run `pd.to_numeric(col, errors='coerce')` on it?  
   `Answer:` ‘25’ and ‘35’ become 25.0 and 35.0, and ‘thirty’ becomes NaN.

10. When would you choose `.dropna()` over `.fillna()`, and vice versa?  
   `Answer:` Drop when the row is useless without that value, like a missing ID or price. Fill when the row is still useful and there’s a sensible fill value, like ‘Unknown’ for a category.

11. A survey stores missing ages as `-1`. Why is that *worse* for analysis than a blank (`NaN`), and what one-line fix turns them into real missing values?  
   `Answer:` Pandas treats -1 as a real number, so it pulls averages down and .isnull() never counts it. Fix: df['age'] = df['age'].replace({-1: np.nan})

12. Two rows share an `order_id` but have different amounts. Will `df.drop_duplicates()` remove one? What argument makes it compare only `order_id`?  
   `Answer:` No, because the rows aren’t exact duplicates. Use subset=['order_id'].

---

### ✏️ Task: Clean a Column

```python
# Using ufo.csv:
# 1. Check .isnull().sum() for the whole dataset.
# 2. Pick the column with the most missing values.
# 3. Decide (and justify in a comment) whether dropping or filling makes more
#    sense for that specific column, then do it.

ufo = pd.read_csv('ufo.csv')
print(ufo.isnull().sum())
# country has the most missing values. Filling makes more sense than dropping because dropping would lose data.
ufo['country'] = ufo['country'].fillna('Unknown')
print(ufo['country'].isnull().sum())   # 0
```

### 🤖 Explain It

In your own words: why might dropping rows with missing data be a bad idea if a large fraction of your dataset has at least one missing value somewhere?

If many rows have at least one missing value somewhere, dropping them all can throw away a large share of the data. On ufo.csv, any-row drops would remove 17% of the rows, mostly over gaps in columns you may not even need. It can also bias the results if the dropped rows have something in common.
---

## 🧱 Section 5: Column Operations, Sorting, and Filtering

13. What's the difference between `df.rename(columns={'a': 'b'})` and `df.columns = ['b', 'c', 'd']`?  
   `Answer:` .rename() changes only the columns you name, so it’s safer. Assigning to df.columns replaces every name at once, and the list has to be exactly the right length and order or names shift onto the wrong columns.

14. Rewrite this bracket-filter as a `.query()` call:
```python
df[(df['math_score'] >= 80) & (df['science_score'] >= 80)]
```
   `Answer:` df.query('math_score >= 80 and science_score >= 80')

15. If `status` is a brand-new column, what do the rows with `score >= 70` contain after `df.loc[df['score'] < 70, 'status'] = 'review'`? How do you give every row a default first?  
   `Answer:` NaN, because nothing was ever assigned to those rows. Give every row a default first: df['status'] = 'ok', then run the .loc[] line.

---

### ✏️ Task: Build a Feature

```python
# Using students.csv:
# 1. Create a "total_score" column (math + science).
# 2. Sort by total_score, descending.
# 3. Print just the top 3 students' first_name and total_score.

students = pd.read_csv('students.csv')
students['total_score'] = students['math_score'] + students['science_score']
students.sort_values('total_score', ascending=False)[['first_name', 'total_score']].head(3)
```

### ✏️ Task: Loop vs. Vectorized

```python
# Using students.csv:
# 1. Build a list of each student's total score with an .itertuples() loop.
# 2. Compute the same totals with one whole-column expression.
# 3. Confirm they match, then use %timeit to compare the two.

import numpy as np

totals = []
for row in students.itertuples():
    totals.append(row.math_score + row.science_score)

students['total_score'] = students['math_score'] + students['science_score']
print('Same result?', np.allclose(totals, students['total_score']))

%timeit [row.math_score + row.science_score for row in students.itertuples()]
%timeit students['math_score'] + students['science_score']
```

### 🤖 Explain It

In your own words: what does "feature engineering" mean in the context of `total_score` or `average_score` — why create a new column instead of just computing the value fresh every time you need it?

Feature engineering means building new columns from existing ones so the data directly holds what you want to analyze. Making total_score once means you can sort, filter, and group by it without rewriting the formula each time, and every later step uses the same definition.
---

## 🧩 Section 6: Grouping and Combining

16. Describe the three steps of `df.groupby('Pclass')['Survived'].mean()` (split, apply, combine) in plain words. What does the result tell you?  
   `Answer:` Split: divide the passengers into groups by class. Apply: average the Survived column in each group. Combine: put the three averages into one result. Since Survived is 1 or 0, the result is the survival rate for each class.

17. What's the difference between `pd.concat()` and `.merge()`, and between a `'left'` and an `'inner'` merge?  
   `Answer:` pd.concat() stacks more rows of the same kind of data. .merge() adds related columns through a shared key. A left merge keeps every row of the left table and fills unmatched ones with NaN. An inner merge keeps only rows whose key is in both tables.

---

### ✏️ Task: Survival by Group

```python
# Using titanic.csv:
# 1. Find the survival rate by Pclass, then by Pclass AND Sex together.
# 2. Use .agg() to show, per Embarked port: passengers, average Fare, survival rate.
# 3. .reset_index() the result and sort it by survival rate, highest first.

print(titanic.groupby('Pclass')['Survived'].mean().round(2))
print(titanic.groupby(['Pclass', 'Sex'])['Survived'].mean().round(2))

by_port = titanic.groupby('Embarked').agg(
    passengers=('PassengerId', 'count'),
    average_fare=('Fare', 'mean'),
    survival_rate=('Survived', 'mean'),
).round(2).reset_index()
by_port.sort_values('survival_rate', ascending=False)
```

### ✏️ Task: Join Two Tables

```python
# Build a table of 5 students (student_id, name) and a table of 4 grades
# (student_id, grade), where one student has no grade.
# Merge them with how='left' and with how='inner'. How many rows does each give, and why?

students_ids = pd.DataFrame({'student_id': [1, 2, 3, 4, 5], 'name': ['Ana', 'Ben', 'Cy', 'Deb', 'Eli']})
grades_ids = pd.DataFrame({'student_id': [1, 2, 3, 4], 'grade': ['A', 'B', 'A', 'C']})

left = students_ids.merge(grades_ids, on='student_id', how='left')
inner = students_ids.merge(grades_ids, on='student_id', how='inner')
print('left:', len(left), 'rows')    # 5, Eli kept with grade NaN
print('inner:', len(inner), 'rows')  # 4, Eli dropped
```

### 🤖 Explain It

In your own words: when you merge UFO sightings (state codes like `'tx'`) with populations (codes like `'TX'`), every state fails to match at first. Why, and what does that teach you about checking keys *before* you join?

Keys have to match exactly, and ‘tx’ and ‘TX’ are different text to Pandas. Before a join, look at a few keys from each table and standardize them first, for example with .str.upper(). After the join, check the row count and look for unmatched NaN values.

---

## 🧾 Submit Checklist

- [ ] I created a `Series` and a `DataFrame` from Python containers (a dictionary or a list of dictionaries).
- [ ] I loaded a local CSV into a DataFrame and inspected it with `.info()` and `.describe()`.
- [ ] I used both `.loc[]` and `.iloc[]` at least once each.
- [ ] I filtered a DataFrame using a compound condition (`&` or `|`).
- [ ] I cleaned at least one column with `.fillna()`, `.dropna()`, or `pd.to_numeric()`.
- [ ] I created a new column and sorted by it.
- [ ] I removed duplicate rows or replaced a placeholder value with `NaN`.
- [ ] I filtered with `.isin()`, `.between()`, or `.str.contains()`.
- [ ] I used a whole-column (vectorized) calculation instead of a row-by-row loop.
- [ ] I summarized groups with `groupby()` (and `.agg()`), and combined tables with `pd.concat()` or `.merge()`.
- [ ] I completed the "Explain It" prompts in my own words.
