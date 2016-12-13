# coding=utf-8
import pandas as pd

# sep: [str], [default=','], [string que fará a separação entre as colunas]
data = pd.read_csv('./data/gastos.csv', sep=';')

# Renaming columns
cols = ['unidade', 'naturaza_da_despesa', 'valor']

data.columns = cols

# Map, Apply
data['valor'] = data['valor'].map(lambda x: x.lstrip('R$').replace(".", "").replace(",", "."))
data['valor'] = data['valor'].apply(pd.to_numeric, errors='coerce')

unidade_valor = data[['unidade', 'valor']]
more_20000 =  data[data['valor'] > 20000.00]

# dados unidade ACERVO BIBLIOGRÁFICO ou natureza AUX. FINANCEIRO ESTUDANTE
f_unidade = (data['unidade'] == 'ACERVO BIBLIOGRÁFICO')
f_natureza = (data['naturaza_da_despesa'] == 'AUX. FINANCEIRO ESTUDANTE')
# print data[(f_unidade | f_natureza)]


# gastos por unidade
grouped = data['valor'].head(7).groupby(data['unidade'])


# print grouped.describe()

# top 5: unidades com mais gastos
def some_fn(x):
    if type(x) is float:
        return 'R$ ' + str(x)
    else:
        return

data = data.applymap(some_fn)
print data.head()
# plot: unidade x gastos

# applymap e New Columns
