# Funções ex03) Soma, subtração, multiplicação, divisão e media entre dois números.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def media_aritmetica(a, b):
    return (a + b)/2

# Programa principal 
def main():
    # Entrada de dados
    numero1 = int(input("Digite o 1º número: "))
    numero2 = int(input("Digite o 2º número: "))

    # Chama as funções somar, subtrair, multiplicar, dividir e media_arit para realizar entre os dois números.
    soma = somar(numero1, numero2)
    subtracao = subtrair(numero1, numero2)
    multiplicacao = multiplicar(numero1, numero2)
    divisao = dividir(numero1, numero2)
    media = media_aritmetica(numero1, numero2)

    # Saída de dados
    print(f"Soma: {numero1} + {numero2} = {soma}")
    print(f"Subtração: {numero1} - {numero2} = {subtracao}")
    print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
    print(f"Divisão: {numero1} / {numero2} = {divisao:.2f}")
    print(f"Media: ({numero1} + {numero2})/2 = {media}")

    
if __name__ == "__main__":
    main()
