"""
ex03) Com a estrutura FOR, mostre os números ímpares entre 1 e 501 na tela.

"""

print("Mostrando os números ímpares entre 1 e 501: ")
for i in range(1, 502):
    if (i % 2 != 0): # números ímpares
        print(i)

