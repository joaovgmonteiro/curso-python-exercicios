"""
Ex01) Faça um aplicação em que o usuário insira 2 números inteiros e o algoritmo responde se o primeiro valor é maior que o segundo valor,, se é maior ou se são iguais

"""

print("Escolha dois números inteiros para descobrir o maior entre eles...")
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

if n1 == n2:
    print(f"{n1} = {n2}")
elif n1 > n2:
    print(f"{n1} > {n2}")
else:
    print(f"{n1} < {n2}")
