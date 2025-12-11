# Ex08) Leia um número inteiro e mostre se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))

if ((num % 2) == 0):
    x = "PAR"
else:
    x = "ÍMPAR"

print(f"O número é {x}")
