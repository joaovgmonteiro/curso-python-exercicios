import pandas as pd 

data_frame = pd.read_csv('ClassicDisco.csv')

# Mostrar somente as 5 primeiras linhas
#print(data_frame.head())

# Mostrar somente as 5 últimas linhas
#print(data_frame.tail())

#print(data_frame.shape) # Imprime a quantidade de linhas e colunas.

# Mostrar os nomes das colunas:
#print(data_frame.columns)

# Mostrar colunas detalhadas
for i, coluna in enumerate(data_frame.columns, start=1):
    print(f"{i}ª Coluna: {coluna}")