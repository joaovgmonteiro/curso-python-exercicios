'''
Ex07) Determinar o maior de três números
'''

def obter_numeros() -> list:
    numeros = []
    for i in range(1,4):
        numero = int(input("Digite o 1º número: "))
        numeros.append(numero)
    return numeros

def descobrir_maior_numero(numeros: list) -> int: # Função desnecessária nesse caso -> Utilizar o max já seria o suficiente para atribuir a maior_numero
    maior = max(numeros)
    return maior

# Programa principal

numeros = obter_numeros()
maior_numero = descobrir_maior_numero(numeros)
print(f"O maior entre os 3 números é {maior_numero}")