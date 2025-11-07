# Teste 5 números e verifica se é par ou ímpar

print("Escolha números para descobrir se é PAR ou ÍMPAR...")
for i in range(1,6):
    n = int(input(f"Digite o {i}º número: "))
    if (n % 2 == 0):
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")
