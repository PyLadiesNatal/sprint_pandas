# coding=utf-8
import pandas as pd

# sep: [str], [default=','], [string que fará a separação entre as colunas]
data = pd.read_csv('../data/gastos.csv', sep=';')

# Renaming columns
cols = ['unidade', 'naturaza_da_despesa', 'valor']
data.columns = cols

if __name__ == '__main__':
    # Imprimindo dados da coluna 'natureza da despesa'
    print data.naturaza_da_despesa
