# ex11) Crie um dicionário vazio e peça ao usuário para inserir 3 pares de país:capital.

paises = {}

print("Insira 3 pares de país: capital para armazenar no dicionário: ")
for i in range(1,4):
    print(f"{i}º par")
    pais: str = input("Digite o nome do país: ")
    capital: str = input("Digite a capital do país: ")
    paises[pais] = capital # Adiciona a chave e o valor escrito pelo usuário


for chave, valor in paises.items():
    print(f"{chave}: {valor}")
