'''
Leia peso e altura de uma pessoa e calcule o IMC. Use try e 
except para tratar erros como entradas inválidas ou altura igual a
zero.
imc < 18.5 = Abaixo do peso
imc < 25= Peso normal
imc < 30 = Sobrepeso
Imc >=30 = Obesidade

'''

def calcular_imc(x, y):
    return x / (y * y)

def classificar_peso(imc):
    if imc < 18.5:
        situacao = "Abaixo do peso"
    elif imc < 25:
        situacao = "Peso normal"
    elif imc < 30:
        situacao = "Sobrepeso"
    else:
        situacao = "Obesidade"
    return situacao


def validar_peso_altura(x):
    if x <= 0:
        raise ValueError("Valor zero ou menor que zero")

# Programa principal    
def main():
    try:
        nome = input("Digite o nome: ")
        peso = float(input("Digite o seu peso: "))
        validar_peso_altura(peso)
        altura = float(input("Digite sua altura: "))
        validar_peso_altura(altura)        
    except ValueError as err: # raise muda a saida desse err - Caso seja <= 0 vai mostrar outra mensagem.
        print(f"Erro: {err}")
    else:
        imc_paciente = calcular_imc(peso, altura)
        situacao_paciente = classificar_peso(imc_paciente)
        print(f"Paciente: {nome} | Peso: {peso}Kg | Altura: {altura}\nIMC: {imc_paciente:.2f} | Classificação: {situacao_paciente}")
    finally:
        print("Fim do programa!")

if __name__ == "__main__":
    main()