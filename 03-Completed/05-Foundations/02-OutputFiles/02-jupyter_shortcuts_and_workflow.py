# %% [markdown]
# # ⚡ 02 - Jupyter Shortcuts and Workflow
# 
# You've been using notebooks since Module 01. This notebook makes you **faster** (keyboard shortcuts) and your notebooks **reliable** (understanding the kernel and execution order).
# 
# ## ✅ Learning Goals
# - Explain what a notebook combines, and how the notebook file differs from the kernel
# - Switch between Command and Edit mode, and use the essential shortcuts
# - Read execution counts and explain why cells can run out of order
# - Use the **Restart & Run All** habit to catch hidden kernel state
# - Use `%history`, `%save`, and `Out[n]` to recover past work
# - Save, name, clear, and export notebooks appropriately
# - Structure an analysis notebook and fix the most common notebook problems
# 
# > **The core habit:** a reliable notebook runs successfully from top to bottom after restarting the kernel.

# %% [markdown]
# ## 1. What Notebooks Are For
# A Jupyter notebook (an `.ipynb` file) combines in one document:
# - Executable **code**
# - Formatted **notes** (Markdown, covered in notebook 04)
# - **Equations**
# - **Charts and images**
# - Saved **outputs**
# 
# That makes notebooks great for exploring data, teaching, and keeping a **reproducible record** of an analysis. Someone else can rerun your steps and get the same results, but only if the notebook is built carefully. Most of this notebook is about doing that.
# 
# Files this notebook creates go into a **`02-OutputFiles`** folder. Run the cell below to create it.

# %%
from pathlib import Path

OUT = Path('02-OutputFiles')
OUT.mkdir(exist_ok=True)

# %% [markdown]
# ## 2. Modes in Jupyter

# %% [markdown]
# Jupyter has two keyboard modes, and the same key does different things in each:
# 
# | Mode | Purpose | Visual clue (VS Code) | Visual clue (classic Jupyter) |
# |---|---|---|---|
# | **Edit mode** | Type inside a cell | Blinking cursor in the cell, and the cell's editor is outlined | Green cell border |
# | **Command mode** | Act on **whole cells**: select, move, create, delete, change type | No cursor; colored bar on the left of the selected cell | Blue cell border |
# 
# Switch:
# - Press `Enter` → Edit mode
# - Press `Esc` → Command mode
# 
# ⚠️ **The #1 beginner frustration:** pressing a shortcut in the wrong mode. In Edit mode, pressing `B` just types the letter "b". **If a shortcut doesn't work, press `Esc` and try again.**

# %% [markdown]
# ✅ **Your Turn**: Click into a cell below, press `Esc`, then `Enter`, a few times, and notice how the cell's appearance changes between the two modes.

# %% [markdown]
# The border around the cell turns blue and the curser appearns within the cell.

# %% [markdown]
# ## 3. Essential Shortcuts

# %% [markdown]
# These work in **Command mode** (press `Esc` first). On a Mac, `Alt` is the `Option` key.
# 
# ### Cells
# 
# | Shortcut | Action |
# |---|---|
# | `A` | Insert a new cell **A**bove |
# | `B` | Insert a new cell **B**elow |
# | `D`, `D` (press twice) | **D**elete the selected cell |
# | `Z` (VS Code: `Ctrl+Z` / `Cmd+Z`) | Undo a cell deletion |
# | `C` / `X` / `V` | Copy / cut / paste a cell (pastes below) |
# | `M` | Change the cell to **M**arkdown |
# | `Y` | Change the cell to code |
# | `L` | Show or hide **l**ine numbers |
# | `Shift` + `↑` / `↓` | Select several cells at once |
# | `Alt` + `↑` / `↓` (VS Code) | Move the cell up / down |
# 
# ### Running
# 
# | Shortcut | Action |
# |---|---|
# | `Shift` + `Enter` | Run the cell and move to the next one |
# | `Ctrl` + `Enter` | Run the cell and **stay** on it |
# | `Alt` + `Enter` | Run the cell and insert a new cell below |
# | `I`, `I` | **I**nterrupt the kernel (stop a cell that's stuck or taking too long) |
# | `0`, `0` | Restart the kernel (classic Jupyter; in VS Code use the **Restart** toolbar button) |
# 
# These are the classic Jupyter shortcuts. VS Code supports most of them, but a few differ. If one doesn't work in VS Code, open **Keyboard Shortcuts** (`Ctrl+K Ctrl+S`, or `Cmd+K Cmd+S` on Mac) and search for "notebook".
# 
# 💡 **Can't remember a shortcut?** Open the **Command Palette** (`Ctrl+Shift+P`, or `Cmd+Shift+P` on Mac) and type part of what you want, such as "restart kernel" or "clear outputs". It also shows the shortcut, so you learn it for next time.

# %% [markdown]
# Practice on this cell. Click it, then press `Shift` + `Enter` to run it and move on. Then come back and try `Ctrl` + `Enter`, which runs it without moving.

# %%
sales = [120, 150, 175]
sum(sales)

# %% [markdown]
# ✅ **Your Turn**: Practice creating, deleting, and changing cell types using only shortcuts (no mouse).

# %% [markdown]
# A inserts a cell above, B inserts one below, M changes a cell to Markdown, Y changes it to code, D D deletes it, and Ctrl+Z brings it back. Shortcuts only work after pressing Esc.

# %% [markdown]
# ## 4. Code Cells and Markdown Cells
# - **Code cells** run Python. The output appears below the cell.
# - **Markdown cells** document the notebook: titles, explanations, and conclusions. Running one (`Shift` + `Enter`) **renders** it as formatted text. Notebook 04 covers Markdown in depth.
# 
# ### Only the Last Line Displays Automatically
# A code cell automatically shows the value of its **last** line only. To see more than one result, use `print()`:

# %%
scores = [82, 91, 76, 88, 95]
len(scores)                  # not shown: it's not the last line
sum(scores) / len(scores)    # shown

# %%
print(len(scores))
print(sum(scores) / len(scores))

# %% [markdown]
# ## 5. Execution Order and the Kernel
# The **kernel** is the Python process running behind the notebook. Each code cell shows an **execution count**, like `[1]`, `[2]`, `[7]`. These numbers show the order cells were **run in**, not where they sit in the notebook. You can run cells in any order, and that's where trouble starts.
# 
# The two cells below are deliberately in the **wrong** order:

# %%
tax_rate = 0.08

# %%
total = 100 * (1 + tax_rate)
total

# %% [markdown]
# ✅ **Your Turn**:
# 1. Run the `total` cell first. You get a `NameError` because `tax_rate` doesn't exist yet.
# 2. Now run the `tax_rate` cell, then the `total` cell again. It works, and the execution counts show that the cells ran out of order.
# 3. Here's the danger: the notebook now **looks** fine, but it would fail for anyone who runs it top to bottom. Fix the order by moving the `tax_rate` cell **above** the `total` cell (`Alt` + `↑` in VS Code, or drag it).

# %% [markdown]
# 🔁 **Before you Restart & Run All:** Run All stops at the first error, so this deliberate error would keep every cell after it from running (see notebook 02). Step 3 above, moving the `tax_rate` cell above the `total` cell, is what fixes it. If you skip that step, Run All stops at the `total` cell and the rest of this notebook never runs.

# %% [markdown]
# ### The Most Important Habit: Restart & Run All
# Before you submit, share, or trust a notebook:
# 1. **Restart** the kernel (this wipes every variable).
# 2. **Run All** cells from top to bottom.
# 3. Confirm that every cell works with nothing left over from earlier.
# 
# In VS Code, use the **Restart** button and then **Run All** in the notebook toolbar. In Jupyter, use *Kernel → Restart Kernel and Run All Cells*.
# 
# This catches notebooks that only work because an old variable is still in memory, and it's exactly what happens when your notebook is graded.

# %% [markdown]
# ## 6. Kernel State vs. Notebook Contents
# | The **notebook file** stores... | The **kernel** stores... |
# |---|---|
# | Cell contents (code and Markdown) | Variables |
# | Outputs, if saved | Imported libraries |
# | Metadata | Defined functions |
# | | The current working directory and other state |
# 
# > **The notebook is the recipe. The kernel is the kitchen** that's currently cooking from it. Tearing a page out of the recipe doesn't un-bake the cake.
# 
# So deleting a cell does **not** delete what it created. The variable lives on in the kernel until you restart (or use `%xdel` / `%reset` from notebook 01).

# %%
message = 'Hello'

# %% [markdown]
# ✅ **Your Turn**:
# 1. Run the `message` cell above, then **delete** it (`Esc`, then `D`, `D`).
# 2. In the cell below, run `message`. It still works!
# 3. Restart the kernel and run the cell below again. Now it's a `NameError`. (After restarting, re-run the `OUT` setup cell in section 1.)
# 4. Undo the deletion (`Z`, or `Ctrl+Z` / `Cmd+Z` in VS Code) to bring the `message` cell back.

# %%
message

# %% [markdown]
# ## 7. History and Saving Code
# The kernel remembers everything you've run in this session, even cells you've since edited or deleted.
# 
# | Command | What it does |
# |---|---|
# | `%history -n` | Show all inputs with their execution numbers |
# | `%history -n 1-5` | Show inputs 1 through 5 |
# | `%history -n -l 10` | Show the **l**ast 10 inputs |
# | `%save file.py 1-5` | Save inputs 1–5 into a Python file |
# | `%rerun 5` | Run input number 5 again |
# | `Out[3]` | The **output** of execution number 3 |
# | `_` | The most recent output |
# 
# These are handy for recovering something you deleted while exploring. But they depend on execution order, so **don't** use `%rerun` or `Out[n]` in a finished notebook.

# %%
# Show the first 5 commands in this session
%history -n 1-5

# %%
# Save history to a file
%save 02-OutputFiles/my_session.py 1-5

# %% [markdown]
# ✅ **Your Turn**: Use `%history -n -l 10` to view the last 10 commands you ran. What do the numbers on the left represent? Then save those inputs to `02-OutputFiles/last10.py`, using the numbers you see. Finally, display an earlier output with `Out[n]`.

# %%
%history -n -l 10

# %%
%save 02-OutputFiles/Last10.py 1-10

# %% [markdown]
# ## 8. Saving, Naming, and Clearing

# %% [markdown]
# ### Saving
# - `Ctrl + S` (`Cmd + S` on Mac) saves the notebook. VS Code can also save automatically: *File → Auto Save*.
# - The workflow you're actually using in this course: save the notebook, then commit and push it with git/GitHub. See `_StartHere` if you need a refresher on that process.
# 
# ### Naming
# Good names say **what** the notebook does and **where** it fits:
# - ✅ `01_data_cleaning.ipynb`, `02_exploratory_analysis.ipynb`, `03_visualizations.ipynb`
# - ❌ `final.ipynb`, `final_final.ipynb`, `really_final_v8.ipynb` (use git for versions instead)
# 
# For bigger projects, move reusable functions into `.py` files and import them (or `%run` them, from notebook 01). Notebooks are great for analysis but awkward for sharing code between projects.
# 
# ### Clearing Outputs
# Outputs are saved **inside** the `.ipynb` file. They can make it huge (especially images and big tables) and can accidentally keep sensitive information. **Clear All Outputs** (a toolbar button in VS Code), then save, removes them.
# - **While exploring:** keep the outputs.
# - **Making a clean template, or sharing sensitive work:** clear the outputs.
# - **Sharing a finished report:** Restart & Run All, then keep the outputs, so readers can see the results without running anything.

# %% [markdown]
# ## 9. Exporting Notebooks
# 
# | Format | Best for |
# |---|---|
# | `.ipynb` | Someone who will **edit and rerun** it |
# | `.html` | A static report anyone can read in a browser |
# | `.pdf` | A printable, fixed-layout submission |
# | `.py` | Turning the code into a reusable script |
# | Markdown (`.md`) | Documentation, or GitHub-friendly text |
# 
# **How:**
# - **VS Code:** click the `...` menu in the notebook toolbar → **Export**, or search for "Export" in the Command Palette.
# - **Jupyter:** *File → Save and Export Notebook As…*
# 
# ⚠️ HTML and `.py` exports work almost everywhere. PDF export usually needs extra software (a LaTeX installation). If it fails, export to HTML, open that in a browser, and **Print → Save as PDF**.

# %% [markdown]
# ✅ **Your Turn**: Export this notebook to **HTML** and to **`.py`**, and save both in `02-OutputFiles`. Open the HTML file in a browser.

# %% [markdown]
# *Note what you observed here.*

# %% [markdown]
# ## 10. A Practical Notebook Structure
# A well-organized analysis notebook reads like a short report, top to bottom:
# 
# ```markdown
# # Title and purpose
# ## Imports and setup
# ## Load data
# ## Inspect and clean data
# ## Analysis
# ## Visualizations
# ## Findings and limitations
# ```
# 
# Put **all imports in the first code cell**. That way, Restart & Run All never hits an import halfway down. Here's the same idea in miniature:

# %%
# Imports and setup
import statistics

# Data
monthly_revenue = [12000, 14500, 13800, 16200]

# Analysis
average_revenue = statistics.mean(monthly_revenue)
best_month = monthly_revenue.index(max(monthly_revenue)) + 1

# Findings
print(f'Average monthly revenue: ${average_revenue:,.2f}')
print(f'Best month: month {best_month}')

# %% [markdown]
# ## 11. Common Problems and Fixes
# 
# | Problem | Likely cause | Fix |
# |---|---|---|
# | `NameError` | A cell that defines the variable hasn't been run | Run the earlier cells, or Restart & Run All |
# | Shortcut does nothing (or types a letter) | Wrong mode | Press `Esc` for Command mode, or `Enter` for Edit mode |
# | Output doesn't match the code | An old output is left over after you edited the code | Rerun the cell, or clear outputs |
# | Notebook works only sometimes | Hidden kernel state, or cells run out of order | Restart & Run All |
# | A cell runs forever (`[*]` never becomes a number) | Infinite loop, or waiting for input | Interrupt (`I`, `I`, or the ■ button) |
# | Chart doesn't appear | Plot cell not run, or `plt.show()` missing | Run the cell, and add `plt.show()` |
# | `FileNotFoundError` | Wrong working directory, or a lingering `%cd` | Check `%pwd` (notebook 01) |
# | Notebook file is huge | Embedded outputs, images, or data | Clear outputs, and load data from files instead |

# %% [markdown]
# ---
# ### Summary
# - Notebooks combine code, notes, equations, charts, and outputs. The notebook is the **recipe**, and the kernel is the **kitchen**.
# - **Edit mode** (`Enter`) is for typing. **Command mode** (`Esc`) is for whole-cell shortcuts. If a shortcut fails, press `Esc`.
# - `A`/`B` insert, `D D` deletes, `M`/`Y` change the cell type, and `Shift+Enter` runs. The Command Palette finds everything else.
# - Execution counts show **run order**, not position. Deleting a cell doesn't delete its variables.
# - `%history`, `%save`, and `Out[n]` recover past work, but not in a finished notebook.
# - Name notebooks clearly, clear outputs when appropriate, and export to HTML/PDF for readers or `.py` for scripts.
# - **Restart & Run All before you submit.** A reliable notebook runs top to bottom from a fresh kernel.

# %% [markdown]
# ## 🏋️ Practice

# %% [markdown]
# ### Practice 1 — Speed Round (easy)
# Using only keyboard shortcuts: insert a new cell below this one, turn it into a Markdown cell, type a short note in it, and run it.

# %% [markdown]
# ### Practice 2 — Reorganize Without a Mouse (medium)
# Insert 3 new cells and type a different number in each. Then, using only the keyboard:
# - Move the bottom cell to the top (`Alt` + `↑` in VS Code).
# - Split one cell in two: put your cursor mid-line and press `Ctrl` + `Shift` + `-`. In VS Code, if that doesn't work, search the Command Palette for "split cell".
# - Select two cells with `Shift` + `↓` and delete them both at once.
# 
# Shortcuts vary slightly by editor, so look one up if it doesn't match.

# %% [markdown]
# ### Practice 3 — Export and Inspect (harder)
# Export this notebook to `.py`. Open the exported file in VS Code and compare it to the notebook — what happened to the Markdown cells?

# %% [markdown]
# ### Practice 4 — Break It, Then Fix It
# Create a new notebook, `02-OutputFiles/broken.ipynb`, with three code cells **in this order**: `print(greeting)`, then `name = 'Graylian'`, then `greeting = f'Hello, {name}!'`. Get it working by running the cells out of order, and note the execution counts. Then Restart & Run All, watch it fail, and fix the **order** so it runs top to bottom from a fresh kernel.

# %% [markdown]
# ## 🔥 Challenge (Optional) — A Mini Report Notebook
# Create a new notebook, `02-OutputFiles/mini_report.ipynb`, that follows the structure from section 10:
# 1. A Markdown **title** and a written **question** you want to answer (for example, "Which day this week did I spend the most time studying?")
# 2. An **imports** cell at the top
# 3. Some made-up **data** in a list
# 4. A **calculation** that answers the question
# 5. A written **conclusion** in Markdown
# 
# **Bonus:** add a simple chart with `matplotlib`. Notebook 07 covers plotting, but `plt.plot(data)` and `plt.show()` are enough for now.
# 
# Then **Restart & Run All** to prove it works from a fresh kernel, and export it to HTML in `02-OutputFiles`.

# %% [markdown]
# ## 📦 Check Your Output Files
# Run this last to see everything you created. Your exported files and practice notebooks should all be inside `02-OutputFiles`. Upload that folder along with this notebook.

# %%
for path in sorted(OUT.rglob('*')):
    print(path)


