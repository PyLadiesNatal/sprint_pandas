# coding=utf-8
from question02 import data

unidade_valor = data[['unidade', 'valor']]
more_20000 = data[data['valor'] > 20000.00]

# dados unidade ACERVO BIBLIOGRÁFICO ou natureza AUX. FINANCEIRO ESTUDANTE
f_unidade = (data['unidade'] == 'ACERVO BIBLIOGRÁFICO')
f_natureza = (data['naturaza_da_despesa'] == 'AUX. FINANCEIRO ESTUDANTE')
print data[(f_unidade | f_natureza)]
