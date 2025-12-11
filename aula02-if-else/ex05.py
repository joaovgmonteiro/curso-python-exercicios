'''
Ex05)
Peça o preço do produto e aplique desconto:
-> 10% se o preço for até R$ 100
-> 20% se for acima de R$ 100
Mostre o novo valor. 
'''

preco_produto = float(input("Informe o preço do produto: "))
if (preco_produto < 0):
    print("Você digitou um preço inválido.")
elif (preco_produto <= 100):
    desconto = (preco_produto) * (10/100) # Retira 10% do valor do produto
else: 
    desconto = (preco_produto) * (20/100) # Retira 20% do valor do produto
valorComDesconto = preco_produto - desconto # Aplica o desconto
print(f"Preço do produto = R${preco_produto} | Desconto aplicado: R${desconto:.2f} ")
print(f"Novo valor após desconto: {valorComDesconto:.2f}")



'''
Versão profes
preco = float(input("Preço: R$ "))
if(preco <= 100):
    desc = preco * 0.1
else: 
    desc = preco * 0.2
novo_valor = preco - desc
print("Preço: R$ ", preco)
print("Desconto: R$ ", desc)
print("Novo Preço: R$ ", novo_valor)

'''