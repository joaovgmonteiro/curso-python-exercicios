'''
Teste 5 entradas de provas, prova01, prova02, prova03.
Faça a média entre as provas e mostra a situação onde:
Média >= 7 aprovado
Média >= 5 recuperação
Média < 5 reprovado
'''
soma = 0
   
# Loop que calcula a media de 3 provas de 5 alunos.
for i in range(1, 6):
    print(f"\n======= Média do aluno {i} =======")
    nome = input("Digite o nome do 1º aluno: ")
    print("Digite a nota das 3 provas...")
    n1 = float(input("Nota 1: ").replace(",","."))
    n2 = float(input("Nota 2: ").replace(",","."))
    n3 = float(input("Nota 3: ").replace(",","."))
    media = (n1 + n2 + n3) / 3
    if (media >= 7):
        cond = "Aprovado"
    elif (media >= 5):
        cond = "Recuperação"
    else:
        cond = "Reprovado"
    print(f"Aluno: {nome} | P1:{n1}|P2:{n2}|P3:{n3} | Media: {media:.2f}".replace(".",",") + f" | Situação: {cond}")

# ctrl + c para o terminal em um input








