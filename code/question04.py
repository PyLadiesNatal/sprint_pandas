# coding=utf-8
from question02 import data


def sum_values(group):
    s = 0
    for v in group:
        s = v + s
    return s


# gastos por unidade
grouped = data['valor'].head(50).groupby(data['unidade']).apply(sum_values)


# print grouped


# grouped.describe().plot(kind="bar")
# plt.show()

# converta o valor float para string e crescente no inicio "R$"
def f_change_value(x):
    if type(x) is float:
        return 'R$ ' + str(x)
    else:
        return x


data = data.applymap(f_change_value)


# 3. Separe a string da coluna 'valor', a moeda (ex.: 'R$') deve ser colocado em uma nova coluna.
def split_string(v):
    data = v.split(' ')
    return data[0], data[1]


#a, b = data['valor'].apply(split_string)
data["moeda"], data["valor"] = zip(*data["valor"].str.split().tolist())

print data.head()
