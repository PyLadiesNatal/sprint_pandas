from question01 import data

import pandas as pd

# Map, Apply
data['valor'] = data['valor'].map(lambda x: x.lstrip('R$').replace(".", "").replace(",", "."))
data['valor'] = data['valor'].apply(pd.to_numeric, errors='coerce')

if __name__ == '__main__':
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
