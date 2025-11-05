'''
Escreva um algoritmo em Python que tenha a entrada de :
Nome e salário Bruto.
Condições:
INSS:
Se o salário bruto >= 3000 desconte 11%
Se o salário bruto >= 2000 desconte 9%
Se o '' < 2000 desconte 8%

Vale Transporte:
Se o salário bruto >= 2000 desconte 6%, caso contrário, desconte 5%.

Bônus:
Se o salário bruto >= 3000, dê um bônus de 300 reais, caso o contrário, dê um bônus de 200 reais.

Cargo:
Se o salário bruto >= 3000 cargo = "Acionista"
Se o salário bruto >= 2000 cargo = "Gerente"
Se o salário bruto < 2000 cargo = "Vendedor"

Salário líquido:
Salário bruto - descontos (inss + vale) + bonus

Use variáveis para guardar os cálculos e o cargo para serem mostrados no final. Mostre, também, o nome e o salário inputados pelo usuário.
'''

nome = input("Digite o nome: ").upper() #lower()
salBruto = float(input("Digite o salário bruto: R$").replace(",",".")) # Replace transformando o que é , em .

# Condições
if salBruto >= 3000:
    descInss = salBruto * (11/100)
    bonus = 300
    descVale = salBruto * (6/100)
    cargo = "ACIONISTA"
elif salBruto >= 2000:
    descInss = salBruto * (9/100)
    bonus = 200
    descVale = salBruto * (6/100)
    cargo = "GERENTE"
else:
    descInss = salBruto * (8/100)
    bonus = 200
    descVale = salBruto * (5/100)
    cargo = "VENDEDOR"

# Calculo do salario liquido
salLiq = (salBruto - (descInss + descVale)) + bonus

# Saída dos dados
print("=" * 30)
print(f"Nome do funcionário: {nome}")
print(f"Salário bruto: R$ {salBruto:.2f}".replace(".",","))
print(f"Cargo: {cargo}")
print(f"Descontado do INSS: - R$ {descInss:.2f}".replace(".",","))
print(f"Descontado do vale transporte: - R$ {descVale:.2f}".replace(".",","))
print(f"Bônus: + R$ {bonus:.2f}".replace(".",","))
print(f"Salário líquido: R$ {salLiq:.2f}".replace(".",","))
print("=" * 30)



'''
Versão prof

nome = input("Nome: ")
salario = float(input("salario: "))

#inss
if salario >= 3000:
    inss = salario * 0.11
elif salario >= 2000:
    inss = salario * 0.09
else:
    inss = salario * 0.08

#vale
if salario >= 2000:
    vale = salario * 0.06
else:
    vale = salario * 0.05

#bonus
if salario >= 3000:
    bonus = 300
else: 
    bonus = 200

#cargo
if salario >= 3000:
    cargo = "Acionista"
elif salario >= 2000:
    cargo = "Gerente"
else:
    cargo = "Vendedor"

salarioLiquido = salario - (inss + vale) + bonus

#saídas:
print(f"Nome: {nome}")
print(f"Salario: {salario}")
print(f"INSS: {inss}")
print(f"Vale: {vale}")
print(f"Bônus: {bonus}")
print(f"Cargo: {cargo}")
print(f"Salário Líquido: {salarioLiquido}")

'''