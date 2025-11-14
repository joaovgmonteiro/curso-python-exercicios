"""
Ex04) Crie uma programa que leia a altura e o peso de N pessoas e mostre seu IMC com a respectiva classificação. O cálculo do IMC deverá ser 
realizado através de uma função que receberá os valores de entrada necessários para o cálculo.
Fórmula --> IMC = PESO / (ALTURA * ALTURA)
Funções: 
calcular_imc
classificar_peso
"""
# Função que calcula o IMC 
def calcular_imc(x, y):
    return (x / (y * y))

# Função que utiliza o IMC(Kg/m2) do paciente para classificar o peso.
def classificar_peso(imc):
    if imc > 40:
        situacao = "Obesidade grau III"
    elif imc > 35:
        situacao = "Obesidade grau II"
    elif imc > 30:
        situacao = "Obesidade grau I"
    elif imc > 25:
        situacao = "Acima do peso"
    elif imc > 18.5:
        situacao = "Peso normal"
    elif imc > 17:
        situacao = "Abaixo do peso"
    else:
        situacao = "Muito abaixo do peso"
    return situacao

# Programa principal
quantidade = int(input("Digite a quantiade de pessoas que deseja calcular o IMC: "))

print("-"*5, "CALCULADORA DE IMC", "-"* 5)
i = 1
while i <= quantidade:    
    nome = input("Digite o nome do paciente: ")
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    # Calcular o IMC
    imc_paciente = calcular_imc(peso, altura)

    # Classificar o peso do paciente
    class_peso = classificar_peso(imc_paciente)

    # Saída de dados
    print(f"\nINFORMAÇÕES DO {i}º PACIENTE")
    print(f"Nome: {nome} | Peso: {peso} | Altura: {altura} | IMC: {imc_paciente:.2f} | Classificação: {class_peso}\n")
    

    i += 1

print("Programa finalizado!")