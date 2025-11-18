# ex09) Crie um dicionário de frutas com suas quantidades. Adicione uma fruta nova e atualize a quantidade de uma existente.

frutas = {
    "banana": 4,
    "maça": 8,
    "uva": 12
}

print("==================")
for chave, valor in frutas.items():
    print(f"{chave}: {valor}")

print("=============")
frutas["mamão"] = 6

for chave, valor in frutas.items():
    print(f"{chave}: {valor}")

print("============")
frutas["uva"] = 2

for chave, valor in frutas.items():
    print(f"{chave}: {valor}")