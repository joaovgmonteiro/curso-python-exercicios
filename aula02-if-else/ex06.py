'''
Ex06)
Peça a média de um aluno (0 a 10).
Se for maior ou igual a 7, mostre "Aprovado";
Se for maior ou igual a 5, mostre "Reprovado";
caso contrário, "Reprovado".
'''

media = float(input("Informe a média do aluno (0 a 10): "))
if (media < 0 or media > 10):
    print("Você digitou uma nota inválida. ")
elif (media >= 7):
    s = "Aprovado"
elif (media >= 5):
    s = "Recuperação"
else:
    s = "Reprovado"
print("Média: ", media, "| Situação: ", s)
