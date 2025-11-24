'''
ex08) Verificar a nota e o conceito
    nota >= 9: "A"
    nota >= 7: "B"
    nota >=5: "C"
    nota < 5: "D"
'''

def conceito_nota(nota: float) -> str:
    if nota >= 9:
        conceito = "A"
    elif nota >= 7:
        conceito = "B"
    elif nota >= 5:
        conceito = "C"
    else:
        conceito = "D"
    return conceito

# programa principal
try:
    nome_aluno = input("Digite o nome do aluno: ")
    nota_aluno = float(input(f"Digite a nota do aluno({nome_aluno}): "))

    conceito = conceito_nota(nota_aluno)

    print(f"Aluno: {nome_aluno} | Nota: {nota_aluno} | Conceito: {conceito}")
except ValueError:
    print("Erro: Valor inválido")