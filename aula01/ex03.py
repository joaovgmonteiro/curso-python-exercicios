# este símbolo comenta apenas 1 linha de código
'''
as áspas simples comenta um bloco de comando
Ex3) O usuário escolhe 2 números inteiros e mostra:
Soma
Subtração
Multiplicação
Divisão
'''

print("Escolha dois números inteiros para ser realizado cálculos...")
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

print("==== Operações ====")
# Variaveis visando o armazenamento futuro
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
divi = n1/n2

print(f"Soma: {n1} + {n2} =", soma) 
print(f"Subtração: {n1} - {n2} =", subtracao)
print(f"Multiplicação: {n1} * {n2} =", multi)
print(f"Divisão: {n1} / {n2} =", divi)


