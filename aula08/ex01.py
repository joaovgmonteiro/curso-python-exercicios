'''
Ex01) Verificar se o número é positivo, negativo ou zero.
'''

def analisar_numero(num: int) -> str:
    if num > 0:
        tipo = "Positivo"
    elif num < 0:
        tipo = "Negativo"
    else:
        tipo = "Zero"
    return tipo


# Programa principal
numero = int(input("Digite um número: "))
print(f"O número é {analisar_numero(numero)}")