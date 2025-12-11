'''
Peça o salário e calcule o imposto:
• Até R$ 2000 → isento
• De R$ 2000,01 a R$ 3500 → 10%
• De R$ 3500,01 a R$ 5000 → 15%
• Acima de R$ 5000 → 20%
Mostre o valor do imposto e o salário líquido.

'''

print("=" * 15, "Imposto de renda", "=" * 15)
sal = float(input("Digite o seu salário: "))

if (sal <= 2000):
    imp = 0
elif (sal >= 2000.01 and sal <= 3500):
    imp = sal * (10/100)
elif (sal >= 3500.01 and sal <= 5000):
    imp = sal * (15/100)
else:
    imp = sal * (20/100)

sal_liq = sal - imp
print(f"Salário: {sal} | Imposto: {imp:.2f} | Salário líquido: {sal_liq:.2f}")