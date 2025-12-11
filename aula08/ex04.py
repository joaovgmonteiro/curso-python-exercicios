# Verificar se o número é par ou ímpar


def classificar_numero(numero):
    if numero % 2 == 0:
        situacao = "par"
    else:
        situacao = "ímpar"
    return situacao

print("Digite um número para descobrir se é par ou ímpar")
numero = int(input("Escolha o número: "))

print(f"O número {numero} é {classificar_numero(numero)}")