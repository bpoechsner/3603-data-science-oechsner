# coding: utf-8
from pathlib import Path

OUT = Path('02-OutputFiles')
OUT.mkdir(exist_ok=True)
sales = [120, 150, 175]
sum(sales)
scores = [82, 91, 76, 88, 95]
len(scores)                  # not shown: it's not the last line
sum(scores) / len(scores)    # shown
print(len(scores))
print(sum(scores) / len(scores))
tax_rate = 0.08
total = 100 * (1 + tax_rate)
total
message = 'Hello'
message
# Show the first 5 commands in this session
get_ipython().run_line_magic('history', '-n 1-5')
# Save history to a file
get_ipython().run_line_magic('save', '02-OutputFiles/my_session.py 1-5')
