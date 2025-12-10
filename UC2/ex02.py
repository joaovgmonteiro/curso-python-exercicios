import pandas as pd 
s = pd.Series([10, 20, 30], index = ["a", "b", "c"])

print(s["b"]) 

print(s[["a", "c"]]) # Retorna valores 10 e 30

print(s[s > 15]) # Retorna apenas valores maiores que 15

print(s * 2) # multiplica todos os valores por 2
print(s + 5)

# Suporte a variáveis nulas
s2 = pd.Series([1, None, 3])
print(s2.isnull()) # identifica valores nulos
print(s2.fillna(0)) # substitui nulos por 0

# Operações aritméticas entre duas séries

s1 = pd.Series([10, 20, 30], index = ["a", "b", "c"])
