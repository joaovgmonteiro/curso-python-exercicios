# Com tupla, faça o mesmo algoritmo da aula anterior.


nome = input("Nome: ")
notas = ()
for i in range(1,4):
    nota = float(input(f"Nota {i}: "))
    notas = notas + (nota, ) # Forma de inserção de notas - Não utliza append em tuplas

media = sum(notas) / 3
# Decidir a situação do aluno: -Aprovado -Recuperação -Reprovado
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else: 
    situacao = "Reprovado"
    
# Saída dos dados
print(f"{i}º Aluno: {nome}\nNota 1: {notas[0]}\nNota 2: {notas[1]}\nNota 3: {notas[2]}\nMédia: {media:.2f}\nSituação Final: {situacao} ".replace(".", ","))
print("Programa finalizado!")