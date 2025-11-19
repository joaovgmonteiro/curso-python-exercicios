'''
Calcular o valor do infresso com base na idade 
idade < 12:
10 
idade <= 18:
    valor = 15
idade > 18
20
idade 
'''

def preco_ingresso(idade: int) -> float:
    if idade < 12:
        valor = 10
    elif idade <= 18:
        valor = 15
    else:
        valor = 20
    return valor

idade = int(input("Digite a idade: "))
preco = preco_ingresso(idade)
print("Preco do ingresso: ", preco)