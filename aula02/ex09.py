# Ex09) Leia três números e exiba o maior deles.

print("Digite três números para descobrir o maior entre eles...")
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))

if (n1 > n2 and n1 > n3):
    maior = n1
elif (n2 > n1 and n2 > n3):
    maior = n2
else: 
    maior = n3

print("O maior número entre os três é", maior)
