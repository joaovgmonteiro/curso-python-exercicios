# ex14) Faça um programa que inverta um dicionário (chaves viram valores e vice-versa).

pessoa = {
    "nome": "joao",
    "idade": 23
}

for chave, valor in pessoa.items():
    aux = chave
    pessoa[chave] = valor
    pessoa[valor] = aux

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")