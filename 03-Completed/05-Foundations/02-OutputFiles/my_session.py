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
