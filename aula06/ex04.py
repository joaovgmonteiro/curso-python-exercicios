"""
Escreva um program em Python que leia um nome e as notas de 10 alunos utilizando a estrutura de repetição while.
Para cada aluno, o programa deve:
1. Solicitar o nome do aluno.
2. Ler 3 notas referentes às suas provas. Colocar as notas dentro de uma lista. uma variavel
3. Calcular a média aritmética desses três notas.
4. Verificar a situação do aluno de acordo com a média:
    - Média maior ou igual a 7 -> Aprovado
    - Média maior ou igual a 5 e menor que 7 -> Recuperação
    - Média menor que 5 -> Reprovado    
5. Exibir o nome do aluno, as três notas, a média e a situação final.
O programa deve repetir esse processo para 10 alunos, utilizando a estrutura while.
"""
i=1
print('-' * 60,"\nPrograma para descobrir situação acadêmica dos alunos")
while i <= 10:
    print("-" * 60)
    nome_aluno = input(f"Digite o nome do {i}º aluno: ")
    notas = []
    # Loop para receber as 3 notas do aluno e adicionar na lista notas.
    for j in range(1,4):        
        nota = float(input(f"Digite a nota {j}: "))
        notas.append(nota)
    # Calcular média
    media = (notas[0] + notas[1] + notas[2])/3
    # Decidir a situação do aluno: -Aprovado -Recuperação -Reprovado
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else: 
        situacao = "Reprovado"
    
    # Saída dos dados
    print(f"{i}º Aluno: {nome_aluno}\nNota 1: {notas[0]}\nNota 2: {notas[1]}\nNota 3: {notas[2]}\nMédia: {media:.2f}\nSituação Final: {situacao} ")
    i += 1

print("Programa finalizado!")