# 📝 Quiz: 05 - Foundations

45 questions covering all 8 Foundations notebooks, in order: magic commands, Jupyter workflow, getting help, Markdown, files and paths, data I/O, plotting with NumPy, and timing. Mix of multiple choice, true/false, code-tracing, and short answer.

This is a conceptual self-check. For hands-on practice writing and running real code, see `Foundations_Quiz.ipynb` in this folder.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Magic Commands (01)

**1.** (Multiple Choice) Which magic command shows your current working directory?
A) `%pwd`  B) `%cd`  C) `%ls`  D) `%dir`

A

**2.** (Short Answer) What's the difference between a line magic (`%pwd`), a cell magic (`%%writefile`), and a shell command (`!ls`)?

% is a line magic that applies to just that one line. %% is a cell magic that applies to the whole cell and must be the first line. ! sends the line to the operating system’s shell.

**3.** (Code Tracing) A folder contains only `a.csv` and `b.txt`. What kind of value is stored in `files`, and what does it contain?
```python
files = !ls
```

An IPython SList, which is a list of strings with one item per line of output: ['a.csv', 'b.txt']

**4.** (True/False) `%cd ..  # go up one folder` moves you to the parent folder.

False. IPython treats # go up one folder as part of the folder name, so it fails.

**5.** (Short Answer) Inside a notebook, why should you install packages with `%pip install` instead of `!pip install`?

%pip installs into the same environment the notebook’s kernel is running in. !pip may use a different Python, so the install “works” but import still fails with ModuleNotFoundError.

**6.** (True/False) `%who` only shows variable *names*, while `%whos` also shows their types and a value summary.

True
---

## Section B — Jupyter Workflow (02)

**7.** (Multiple Choice) In Command mode, which keyboard shortcut inserts a new cell *below* the current one?
A) `A`  B) `B`  C) `D D`  D) `M`

B

**8.** (Short Answer) What's the practical difference between Command mode and Edit mode? You press `B` and the letter "b" appears in your code. What happened, and what should you press?

Command mode acts on whole cells (insert, delete, move, change type). Edit mode is for typing inside a cell. You were in Edit mode, so B typed the letter. Press Esc to switch to Command mode, then press B.

**9.** (Code Tracing) What does this cell display when it runs?
```python
x = 5
x * 2
x * 3
```

15

**10.** (Short Answer) A cell near the bottom of a notebook shows `[7]`, and the cell above it shows `[9]`. What does that tell you?

The cells were run out of order. The cell above was run more recently than the one below it.

**11.** (True/False) If you delete the cell that created the variable `message`, `message` is removed from memory immediately.

False

**12.** (Short Answer) Why should you **Restart & Run All** before submitting a notebook?

It proves the notebook runs top to bottom from a fresh kernel with no hidden leftover variables, which is exactly how it will be graded.

---

## Section C — Getting Help (03)

**13.** (Short Answer) `?` shows a docstring. What does `??` sometimes show that `?` doesn't, and why doesn't it always work?

?? shows the actual source code. It doesn’t always work because built-ins and much of NumPy are written in C, so there’s no Python source to show.

**14.** (Multiple Choice) The signature is `sorted(iterable, /, *, key=None, reverse=False)`. Which call is valid?
A) `sorted(iterable=nums)`  B) `sorted(nums, None, True)`  C) `sorted(nums, reverse=True)`  D) `sorted()`

C

**15.** (Code Tracing) What error does this raise, and what does it mean?
```python
numbers = [1, 2, 3]
numbers.mean()
```

AttributeError: 'list' object has no attribute 'mean'. Python lists don’t have a .mean() method; NumPy arrays do.

**16.** (Short Answer) A long traceback fills the screen. Which line should you read first, and why?

The last line. It names the error type and explains what went wrong.

**17.** (Short Answer) What does `dir(obj)` give you that Tab completion doesn't?

A real Python list of every name the object has, which you can filter and search with code.

---

## Section D — Markdown (04)

**18.** (Short Answer) What's the Markdown syntax for a level-2 heading (like `## Section 2`)?

## Heading text

**19.** (Short Answer) How do you write **inline** LaTeX math in a Markdown cell, versus a **block** equation on its own line(s)?

Inline math goes between single dollar signs, $...$. A block equation goes between double dollar signs, $$...$$, on its own lines.

**20.** (Short Answer) The Markdown text `The item costs $5 and the tax is $2.` renders strangely. Why, and how do you fix it?

$ starts LaTeX math, so the text between the two dollar signs renders as math. Escape them with a backslash: \$5 and \$2.

**21.** (Short Answer) You typed two lines directly under each other in a Markdown cell, but they render as **one** line. Name two ways to fix it.

Put a blank line between them for a new paragraph, or use a <br> tag (ending the line with two spaces also works).

**22.** (Short Answer) Why might you add narrative Markdown cells between code cells instead of just writing code comments?

Markdown cells explain the reasoning and results in formatted, readable text, so the notebook reads like a report. Readers don’t have to dig through code comments to understand it.

---

## Section E — Files and Paths (05)

**23.** (Code Tracing) What does this print?
```python
with open('x.txt', 'w', encoding='utf-8') as f:
    f.write('hi')

with open('x.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```

hi

**24.** (Multiple Choice) Which file mode adds to the end of an existing file **without** erasing it?
A) `'r'`  B) `'w'`  C) `'a'`  D) `'x'`

C

**25.** (Code Tracing) What does this print?
```python
from pathlib import Path
p = Path('data') / 'sales_2026.csv'
print(p.name, p.stem, p.suffix)
```

sales_2026.csv sales_2026 .csv

**26.** (Short Answer) Why is it good practice to use a relative path (like `'data/file.csv'`) instead of an absolute path (like `'C:/Users/yourname/...'`) in a notebook you'll share or submit?

An absolute path only exists on your computer, so it breaks for anyone else, including the grader. A relative path works anywhere the same folder layout exists.

**27.** (Code Tracing) `scores.csv` contains the two lines `Name,Score` and `Alice,90`. What does this print, and why might that cause a problem?
```python
import csv
with open('scores.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))
print(rows[1])
```

['Alice', '90']. The score comes back as the string '90', so math on it fails or does string concatenation until you convert it with int().

**28.** (True/False) After saving `{'point': (3, 4)}` with `json.dump` and reading it back with `json.load`, you get back exactly the same dictionary.

False

---

## Section F — Data Input and Output (06)

**29.** (Short Answer) What does `pd.read_csv('file.csv')` return?

A DataFrame.

**30.** (Multiple Choice) Which DataFrame method shows summary statistics (mean, standard deviation, min/max, etc.)?
A) `.head()`  B) `.info()`  C) `.describe()`  D) `.columns()`

C

**31.** (Short Answer) You save a DataFrame with `df.to_csv('out.csv')`, read it back, and find an extra `Unnamed: 0` column. What caused it, and how do you prevent it?

The DataFrame’s index was saved as an extra unnamed column. Prevent it with df.to_csv('out.csv', index=False).

**32.** (Short Answer) What does JSON written with `orient='records'` look like, and why is it usually the layout you want?

A list with one dictionary per row, like [{"Name": "Alice", "Score": 90}, ...]. It matches how most APIs return data and is easy to read and reuse.

**33.** (Short Answer) After `pd.read_csv`, the ZIP code `02108` shows up as `2108`. Why, and how do you fix it?

Pandas read the column as an integer, which drops the leading zero. Fix it with pd.read_csv('file.csv', dtype={'Zip': str}).

**34.** (Short Answer) What does `pd.read_excel('file.xlsx', sheet_name=None)` return?

A dictionary of {sheet name: DataFrame}, one entry for every sheet in the workbook.

---

## Section G — Plotting with NumPy and Matplotlib (07)

**35.** (Code Tracing) What do these two lines print?
```python
print([1, 2] * 2)
print(np.array([1, 2]) * 2)
```

[1, 2, 1, 2] and [2 4]

**36.** (Matching) Choose the best chart (line, bar, scatter, or histogram) for each question:
a) Which department sold the most?
b) How did daily website visits change over a month?
c) Is there a relationship between price and units sold?
d) What is the distribution of customer order values?

a) bar, b) line, c) scatter, d) histogram

**37.** (Short Answer) A histogram and a bar chart both draw rectangles. What's the difference in what they show?

A histogram groups one numeric variable into ranges (bins) to show its distribution, and its bars touch along a number line. A bar chart compares separate categories.

**38.** (Short Answer) You call `plt.show()` and then `plt.savefig('chart.png')`, and the saved image is blank. Why?

plt.show() finishes and clears the figure, so savefig afterwards saves an empty one. Call savefig before plt.show().

**39.** (Short Answer) On a box plot, what does the line **inside** the box represent, and what do the dots **beyond** the whiskers represent?

The line inside the box is the median. The dots beyond the whiskers are possible outliers, values more than 1.5 × IQR outside the box.

---

## Section H — Timing and Performance (08)

**40.** (Short Answer) What's the difference between `%time` and `%timeit`, and why is `%timeit` more trustworthy for comparisons?

%time runs the code once. %timeit runs it many loops over several runs and reports the mean ± standard deviation. That averages out background noise, so it’s more trustworthy for comparisons.

**41.** (Short Answer) Why is a NumPy vectorized operation like `arr ** 2` usually much faster than a Python `for` loop doing the same calculation element by element?

NumPy makes one call and does the loop in fast compiled code. A Python loop handles each element as a Python object, checking types and looking up the operation on every pass.

**42.** (True/False) A variable created inside a `%%timeit` cell is available in the cells after it.

False

**43.** (Short Answer) What's unfair about comparing `%timeit np.array(my_list) ** 2` against `%timeit arr ** 2` to decide whether squaring is fast?

The first timing also includes converting the list to an array every time, so it isn’t measuring squaring alone. The comparison isn’t the same work.

**44.** (Short Answer) Why is `[s / max(scores) for s in scores]` slow for large lists? How would you fix it, and roughly what happens to its runtime when the list doubles in size?

max(scores) rescans the whole list for every element, so the work grows with n². Fix it by computing top = max(scores) once before the loop and using [s / top for s in scores]. When the list doubles in size, the slow version takes about 4x as long, and the fixed version only about 2x.

**45.** (Multiple Choice) What does `%prun` show you?
A) Only the total time of the cell  B) How much time was spent in each function called  C) How much memory each variable uses  D) The source code of a function

B

