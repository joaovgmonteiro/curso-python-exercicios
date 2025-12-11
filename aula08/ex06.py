'''
Ex06) Calcular desconto de produto:
    valor >= 500:
        recebe 9% de desconto
    valor >= 200:
        recebe 8% de desconto
    valor < 200:
        recebe 7% de desconto

'''

def calcular_desconto(valor: float) -> float:
    if valor >= 500:
        desconto = valor * 0.09
    elif valor >= 200:
        desconto = valor * 0.08
    else:
        desconto = valor * 0.07
    return desconto


# Programa principal 
valor_produto = float(input("Informe o valor do produto para descobrir o desconto: "))
desconto_produto = calcular_desconto(valor_produto)

print(f"Valor do produto: R${valor_produto}")
print(f"desconto: R${desconto_produto:.2f}")
print(f"Novo valor após aplicar o desconto: R${valor_produto - desconto_produto}")
