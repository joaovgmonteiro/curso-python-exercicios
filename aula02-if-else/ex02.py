# O usuário entra com dois valores inteiros e o programa responde quem é o maior entre eles.

print("Digite dois valores inteiros para descobrir qual o maior entre eles...")
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

print("=" * 30)
print("n1= ",n1, "\nn2= ", n2)
print("=" * 30)

if (n1 > n2):
    print("O 1º número é maior que o 2º.")
elif (n1 == n2):
    print("Os dois números são iguais.")
else:
    print("O 2º número é maior que o 1º.")

# Poderia usar o f= format para mostrar os valores na string. Ex.: print(f"{n1} é maior que {n2}")
# {} interpolação -> Valor da variavel em uma string.

'''
1ª Versão do profes.
x = int(input("Escolha o 1º valor: "))
y = int(input("Escolha o 2º valor: "))

if (x>y):
    print("O primeiro valor é maior que o segundo.")
else:
    print("O segundo valor é maior que o primeiro.")


2ª Versão profes.
x = int(input("Escolha o 1º valor: "))
y = int(input("Escolha o 2º valor: "))

if (x>y):
    print(n1, "é maior que ",n2)
else:
    print(n2, "é maior que ",n1)

'''

