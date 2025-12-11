pessoa  = {
    "nome": "João Victor Monteiro",
    "idade": 23,
    "cidade": "Niterói"
}


# Acessar valores
print(pessoa["nome"])
print(pessoa.get("idade"))

#iteração
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Adicionar/Modificar
pessoa["profissão"] = "Programador"
pessoa["idade"] = 26

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#remover 

del pessoa["cidade"]

#ou
pessoa.pop("profissão")

# Verificar se chave existe
if "idade" in pessoa:
    print("A chave existe!")