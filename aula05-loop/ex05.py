# Teste 5 números e verifica se é par ou ímpar

for i in range(0,5):
    n = int(input("Digite um número: "))
    if (n % 2 == 0):
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")
