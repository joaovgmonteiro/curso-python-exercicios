import pandas as pd 

cargos = []
salarios = []
qtd = int(input("Deseja cadastrar quantas vezes? "))

for i in range(qtd):
    print(f"Cadastro: {i}")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    cargos.append(cargo)
    salarios.append(salario)

dados = {
    'cargos': cargos,
    'salarios': salarios
}

dados_bi = pd.DataFrame(dados)
print(dados_bi)
