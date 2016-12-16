# coding=utf-8
from question02 import data

import pandas as pd


def sum_values(group):
    s = 0
    for v in group:
        s = v + s
    return s


# gastos por unidade
grouped = data['valor'].head(7).groupby(data['unidade']).apply(sum_values)
print grouped


# grouped.describe().plot(kind="bar")
# plt.show()

# converta o valor float para string e crescente no inicio "R$"
def f_change_value(x):
    if type(x) is float:
        return 'R$ ' + str(x)
    else:
        return

data = data.applymap(f_change_value)
# print data.head()

# applymap e New Columns
