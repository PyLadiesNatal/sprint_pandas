### Let The Games Begin

1. Primeiros passos...

    a. Abrar o arquivo .csv

    b. Renomeio as colunas para 'unidade', 'naturaza_da_despesa', 'valor'.  

    c. Imprima todos os dados 

    **BUM**: Error tokenizing data, certo? Procure entre os argumentos usados no método read_csv até encontrar qual poderia ajudar.
 
2. Aplicanto mudanças...  

    a. Altera as strings da coluna valor, por exemplo: "R$ 10.842,74" para "10842.74"

    b. Mudar o formado da coluna valor para float

3. Indexando e filtrando dados

    a. Exiba somente a coluna de 'unidade' e 'valor'

    b. Huuum... exiba somente os registros em que a valor gasto foi maior que 2500.0

    c. Imprima os dados onde o valor da unidade é 'ACERVO BIBLIOGRÁFICO' ou natureza AUX. é 'FINANCEIRO ESTUDANTE'
    
4. Criando funções 

    a. Crie uma função que converta o valor float para string e crescente no inicio "R$"
    
5. Agrupe os valores pelas unidades

6. Separe a string da coluna 'unidade', o valor ID inicial (ex.: 0106/2011) deve ser colocado em uma nova coluna.