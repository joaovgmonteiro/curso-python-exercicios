# ex08) Crie um dicionário com seus dados pessoais (nome, idade, cidade, hobby) e imprima cada informação.

pessoa = {
    "nome": "João Victor",
    "idade": 23,
    "cidade": "Niterói",
    "hobby": "Volei"

}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# print(f"nome: {pessoa["nome"]}") 