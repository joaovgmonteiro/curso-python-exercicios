'''
O usuário entra com dois valores inteiros e o programa responde se:
1º valor é maior que o 2º valor
2º valor é maior que o 1º valor
1º valor é igual ao 2º valor
'''

x = int(input("Escolha o 1º valor: "))
y = int(input("Escolha o 2º valor: "))
if (x == y):
    print(f"O número {x} é igual ao número {y}")
elif (x > y):
    print(f"O número {x} é maior que o número {y}")
else:
    print(f"O número {y} é maior que o número {x}")
