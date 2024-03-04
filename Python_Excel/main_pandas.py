import pandas as pd

# Pandas NÂO mantém gráficos nem fórmulas de células
"""
Objetivos: 
Atualizar o imposto para 1,5 onde o tipo é serviço
Atualizar o preço base
"""

table = pd.read_excel('Produtos.xlsx')

# [Linha, coluna]
table.loc[table['Tipo'] == 'Serviço', 'Multiplicador Imposto'] = 1.5 # Atualiza o valor para 1.5

table['Preço Base Reais'] = table['Preço Base Original'] * table['Multiplicador Imposto'] # Calcula novamente o valor do imposto para cada linha

table.to_excel('Produtos_pandas.xlsx', index=False)