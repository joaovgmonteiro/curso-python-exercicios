"""
ex05) Com a estrutura FOR, faça uma aplicação em que o usuário escolhe 10 números e o algoritmo responde se é par ou ímpar.
"""

print("-" * 60,"\nEscolha números inteiros para descobrir se são PAR ou ÍMPAR\n", "-" * 60)

for i in range(1,11):
    numero = int(input(f"Escolha o {i}º número: "))
    if numero % 2 == 0:
        situacao = "PAR"
    else:
        situacao = "ÍMPAR"
    print(f"O número {numero} é {situacao}")

print("Programa finalizado!")

# Fazer o teste com try except dentro do for. Fazer algum jeito para caso ocorra uma entrada inválida na iteração não ocorra o i = i + 1 
# e sim permaneça na interação até um valor válido ser recebido.

