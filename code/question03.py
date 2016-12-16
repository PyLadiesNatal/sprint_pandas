from question01 import data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Map, Apply
data['valor'] = data['valor'].map(lambda x: x.lstrip('R$').replace(".", "").replace(",", "."))
data['valor'] = data['valor'].apply(pd.to_numeric, errors='coerce')

unidade_valor = data[['unidade', 'valor']]
more_20000 =  data[data['valor'] > 20000.00]

# np.isclose(v, max):
lista = data['valor']
max_value = 0.0
for i in range(0, len(lista) - 1):
    try:
        v = lista[i]
        if v > max_value:
            max_value = v
    except:
        continue

print max_value
# 1194197292.62



# dados unidade ACERVO BIBLIOGRÁFICO ou natureza AUX. FINANCEIRO ESTUDANTE
f_unidade = (data['unidade'] == 'ACERVO BIBLIOGRÁFICO')
f_natureza = (data['naturaza_da_despesa'] == 'AUX. FINANCEIRO ESTUDANTE')
# print data[(f_unidade | f_natureza)]

def some(group):
    s = 0
    for v in group:
        s = v + s
    return s

# gastos por unidade
grouped = data['valor'].head(7).groupby(data['unidade']).apply(some)

"""
t = np.arange(data.unidade)
s = np.sin(data.valor)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
"""

grouped.describe().plot(kind="bar")
#plt.show()


print grouped

# top 5: unidades com mais gastos
def some_fn(x):
    if type(x) is float:
        return 'R$ ' + str(x)
    else:
        return

data = data.applymap(some_fn)
# print data.head()
# plot: unidade x gastos

# applymap e New Columns
