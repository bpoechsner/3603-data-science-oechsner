# 📝 Quiz: 06 - Working with Data (Advanced)

47 questions covering Pandas Series/DataFrames, loading/exploring data, indexing/selection, cleaning, column operations, sorting/filtering/searching, grouping and combining tables, and a "going further" bonus. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Series and DataFrames

**1.** (Short Answer) What's the difference between a Pandas `Series` and a `DataFrame`?  

A Series is one labeled column of values. A DataFrame is a table of rows and columns, where each column is a Series that shares the same index.

**2.** (Code Tracing) What prints?
```python
s = pd.Series({'a': 1, 'b': 2})
print(s['a'])
```  
1

**3.** (Short Answer) What does `df.shape` return?

A tuple of (rows, columns).

**4.** (Short Answer) If you add two `Series` together and one has a label the other doesn't, what happens at that label?

That label becomes NaN, because Pandas lines up values by label and there’s nothing to add it to.

**5.** (Short Answer) You have a list of dictionaries, one per student (the way you stored records in Module 03b). What does `pd.DataFrame(that_list)` turn each dictionary into?

Each dictionary becomes a row, and the keys become the column names.

**6.** (Code Tracing) What prints?
```python
scores = pd.Series([70, 95, 88])
print(scores[scores > 80].tolist())
```

[95, 88]

---

## Section B — Loading and Exploring Data

**7.** (Multiple Choice) Which method shows summary statistics (mean, std, min/max) for numeric columns?
A) `.head()`  B) `.columns`  C) `.describe()`  D) `.shape`

C

**8.** (Short Answer) What's the difference between what `.head()` and `.info()` each tell you about a DataFrame?

.head() shows the first few rows of actual data. .info() shows the structure: row count, column names, non-null counts, and dtypes.

**9.** (Short Answer) How do you count how many missing values are in *each column* of a DataFrame?

df.isnull().sum()

**10.** (Short Answer) What do `df.duplicated().sum()` and `df['col'].value_counts(dropna=False)` each tell you?

df.duplicated().sum() counts how many rows are exact copies of an earlier row. value_counts(dropna=False) shows every distinct value in the column and how often it appears, including missing values.

**11.** (Short Answer) Titanic's `Age` column holds whole numbers, but its dtype is `float64`. Why?

It has missing values, and NaN only exists as a float, so the whole column is stored as float64.

---

## Section C — Indexing and Selection

**12.** (Short Answer) What's the difference between `.loc[]` and `.iloc[]`?

.loc[] selects by label (index values and column names). .iloc[] selects by position (0, 1, 2, ...).

**13.** (Short Answer) Is `df.loc[0:4]` inclusive or exclusive of row `4`? What about `df.iloc[0:4]` and position `4`?

.loc[0:4] is inclusive, so it includes row 4. .iloc[0:4] is exclusive, so it stops before position 4.

**14.** (Short Answer) What symbols does Pandas require for combining conditions when filtering a DataFrame (instead of the `and`/`or` keywords)?

& for and, | for or, ~ for not, with each condition in its own parentheses.

**15.** (Short Answer) What does `df[df['Age'] < 10]` return?

A DataFrame with only the rows where Age is less than 10.

**16.** (Short Answer) Rewrite `df[(df['Embarked'] == 'C') | (df['Embarked'] == 'Q')]` using `.isin()`. Does `df['Age'].between(13, 19)` include ages 13 and 19?

df[df['Embarked'].isin(['C', 'Q'])]. Yes, .between() includes both 13 and 19.

**17.** (Multiple Choice) Which one returns a `DataFrame` rather than a `Series`?
A) `df['Age']`  B) `df[['Age']]`  C) `df.Age`  D) `df.loc[0]`

B

**18.** (Short Answer) After `by_id = df.set_index('PassengerId')`, what does `by_id.loc[2]` select, and how is that different from `df.loc[2]`?

It selects the passenger whose PassengerId is 2. df.loc[2] selects the row labeled 2 in the default index, which is the third row (PassengerId 3).

**19.** (Code Tracing) After `by_id = titanic.set_index('PassengerId')`, do `by_id.loc[3]` and `by_id.iloc[3]` select the same passenger? Why or why not?

No. by_id.loc[3] selects the row labeled 3, which is passenger #3. by_id.iloc[3] selects the row at position 3, which is the 4th row (passenger #4).

**20.** (Short Answer) Write a filter for passengers who did **not** board at Southampton (`'S'`), using `~` and `.isin()`.

df[~df['Embarked'].isin(['S'])]

**21.** (Short Answer) What's wrong with `df[df['Age'] < 10]['child'] = True`, and what should you write instead?

df['child'] = False
df.loc[df['Age'] < 10, 'child'] = True

---

## Section D — Cleaning

**22.** (Short Answer) What's the difference between `.dropna()` and `.fillna()`?

.dropna() removes rows (or columns) that have missing values. .fillna() keeps them and replaces the missing values with something you choose.

**23.** (Short Answer) What does `pd.to_numeric(col, errors='coerce')` do to a value like `'ninety'` in that column?

It turns ‘ninety’ into NaN instead of raising an error.

**24.** (True/False) `NaN` and an empty string `""` are always treated identically by `.isnull()`.

False

**25.** (Short Answer) Two rows have the same `order_id` but different `amount`s. Does `df.drop_duplicates()` remove one of them? What would you write to keep only the last row for each `order_id`?

No, because the rows aren’t exact duplicates. To keep the last row per order_id: df.drop_duplicates(subset=['order_id'], keep='last')

**26.** (Short Answer) A survey stores missing ages as `-1`. Why is that a problem for `df['age'].mean()`, and how do you fix it?

Pandas treats -1 as a real age, so it drags the mean down. Replace it with a real missing value first: df['age'] = df['age'].replace({-1: np.nan})

**27.** (Short Answer) A date column holds `'2022-01-01'`, `'2022/03/01'`, and `'April 5, 2022'`. Why can `pd.to_datetime(col, errors='coerce')` turn two perfectly valid dates into `NaT`, and how do you fix it?

Pandas guesses the format from the first value and turns anything that doesn’t match it into NaT, without any warning. Use format='mixed'.

**28.** (Short Answer) Why does `.astype('int64')` fail on a column with missing values, while `.astype('Int64')` works?

int64 can’t hold missing values, so the conversion fails. Int64 is Pandas’ nullable integer type, and it stores missing values as <NA>.

**29.** (Short Answer) Before deleting rows with a repeated `order_id`, why would you look at `df[df.duplicated(subset=['order_id'], keep=False)]` first?

It shows every copy side by side, so you can tell whether they’re true duplicates or something else, like a correction or a second purchase, before you delete anything.

---

## Section E — Column Operations, Sorting, Filtering, and Searching

**30.** (Short Answer) How do you create a new column that's the sum of two existing numeric columns?

df['total'] = df['a'] + df['b']

**31.** (Short Answer) What does `.apply()` do that you could also do with a `for` loop over rows — and why is `.apply()` usually preferred?

.apply() runs a function on every value in a column without you writing the loop. It’s shorter and clearer, but it’s still a loop under the hood, so a whole-column operation is better when one exists.

**32.** (Short Answer) What does `ascending=False` do inside `df.sort_values(by='score', ascending=False)`?

It sorts from highest to lowest.

**33.** (Short Answer) What's the main advantage of `.query()` over bracket-based boolean filtering (`df[df['col'] > 5]`)?

It’s easier to read, especially with long conditions. You write and/or and plain column names instead of repeating df[‘col’] with & and |.

**34.** (Code Tracing) `bonus` is a brand-new column. What value do the rows with `score >= 80` get in it?
```python
df.loc[df['score'] < 80, 'bonus'] = 5
```

NaN. Nothing was ever assigned to those rows.

**35.** (Short Answer) To compute `price * qty` for every row, why should you write `df['price'] * df['qty']` instead of looping with `.iterrows()`? When *is* a loop (preferably `.itertuples()`) the right tool?

The whole-column version is shorter, clearer, and much faster. A loop is the right tool when each row needs an action instead of a calculation, like writing a file or sending a message for each row.

**36.** (Short Answer) What do `case=False` and `na=False` each do in `df['name'].str.contains('an', case=False, na=False)`?

case=False ignores capitalization. na=False treats missing values as no match, so the filter doesn’t fail.

**37.** (Code Tracing) A student has `math = 95` and `average = 91`. What is their `award` after these three lines, and what would it be if the last two lines were swapped?
```python
df['award'] = 'None'
df.loc[df['average'] >= 85, 'award'] = 'Honor Roll'
df.loc[df['math'] >= 90, 'award'] = 'Math Star'
```

Math Star. If the last two lines were swapped, it would be Honor Roll, because the last rule that matches wins.

**38.** (Short Answer) What does `pd.cut(df['score'], bins=[0, 70, 90, 101], labels=['Low', 'Mid', 'High'], right=False)` do, and why is it usually better than `.apply()` with an `if`/`elif` function for the same job?

It sorts each score into a band: Low for 0 up to 70, Mid for 70 up to 90, and High for 90 up to 101. right=False means each band includes its left edge but not its right. It’s better because it works on the whole column at once instead of calling a function for every value.

**39.** (Short Answer) What's the difference between `df.query('math_score >= minimum')` and `df.query('math_score >= @minimum')`?

Without @, Pandas looks for a column named minimum. With @, it uses the Python variable named minimum.

**40.** (Code Tracing) What does each line return, and why are they different?
```python
books = pd.Series(['C++ Primer', 'C Programming'])
books.str.contains('C++').tolist()
books.str.contains('C++', regex=False).tolist()
```

The first line returns [True, True], because + is a special pattern character, so ‘C++’ matches any C. The second returns [True, False], because regex=False searches for the literal text C++.

---

## Section F — Grouping and Combining

**41.** (Code Tracing) What does this return?
```python
df = pd.DataFrame({'team': ['A', 'B', 'A', 'B'], 'points': [10, 4, 20, 6]})
df.groupby('team')['points'].mean()
```

team
A    15.0
B     5.0
Name: points, dtype: float64

**42.** (Short Answer) Write a `groupby` with `.agg()` that gives, for each `team`, the number of rows and the total `points`, as columns named `games` and `total`.

df.groupby('team').agg(
    games=('points', 'count'),
    total=('points', 'sum'),
)

**43.** (Short Answer) When would you use `pd.concat()` instead of `.merge()`? What does `ignore_index=True` do?

pd.concat() is for stacking more rows of the same kind of data, like one month’s file on top of another. .merge() adds related columns through a shared key. ignore_index=True renumbers the rows 0, 1, 2, ... so labels aren’t repeated.

**44.** (Short Answer) In `orders.merge(prices, on='product_id', how='left')`, what happens to an order whose `product_id` isn't in `prices`? What would `how='inner'` do instead? And why does a merge on state codes fail when one table uses `'tx'` and the other uses `'TX'`?

With how='left', the order is kept and its price columns are NaN. With how='inner', the order is dropped. The ‘tx’/’TX’ merge fails because keys have to match exactly, and Pandas treats ‘tx’ and ‘TX’ as different values.

**45.** (Short Answer) In Titanic, `groupby('Pclass').size()` gives 216 for 1st class, but `groupby('Pclass')['Age'].count()` gives 186. Why are they different?

.size() counts every row in each group. .count() only counts the non-missing values in Age, and 30 first-class passengers have no recorded age.

**46.** (Short Answer) `purchases` has 6 rows. After `purchases.merge(buyers, on='buyer_id', how='left')`, it has 8. What probably happened, and how can `validate=` protect you?

A buyer_id appears more than once in buyers, so the matching purchases were copied once for each duplicate. Using validate='many_to_one' makes Pandas raise an error instead of silently duplicating rows.

---

## Section G — Going Further (Bonus)

**47.** (Short Answer) What do the `usecols` and `nrows` arguments to `pd.read_csv()` do, and when would you reach for them?

usecols loads only the columns you list, and nrows loads only the first N rows. They’re useful when a file is very large and you only need part of it, like ufo.csv.

