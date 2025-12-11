# ex13) Dado um dicionário de produtos com preços, crie uma função que aplique 10% de desconto em todos os produtos.

def aplica_desconto(prod):
    for chave, valor in produtos.items():
        desconto = valor * 0.1
        valor_com_desconto = valor - desconto
        prod[chave] = valor_com_desconto
    
    return prod

produtos = {
    "tv": 1200,
    "pc": 3900,
    "som": 250,
    "roteador": 199
}

# Aplica 10 % de desconto em todos os produtos
produtos_10desconto = aplica_desconto(produtos)

print("Valores dos produtos após aplicar 10 % de desconto")
print(produtos_10desconto.items())