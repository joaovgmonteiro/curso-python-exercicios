'''
ex02) Verificar se o aluno foi aprovado
    média >= 7 aprovado
    média >= 5 recuperação
    média < 5 reprovado

    
'''


def calcular_media(alunos: dict) -> float:
    for chave, valor in alunos.items(): 
        media = sum(valor)/len(valor)
    return media

def situacao_academica(media: float) -> str:
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return situacao

# Utilizei dicionário para armazenar o nome do aluno e o seu conjunto de notas. 
def obter_notas() -> dict:
    nome_aluno = input("Digite o nome do aluno: ")
    notas = []
    for i in range(1,4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    # Adiciona o nome do aluno como chave e sua lista notas como valor em um dicionário. Isso permite que se possa adicionar vários alunos. 
    alunos = {
        nome_aluno: notas
    }
    return alunos

def exibir_relatorio(
        alunos: dict,
        media: float,
        situacao: str
) -> None:
    print("=" * 30)
    for chave, valor in alunos.items(): # Essa saída de dados funciona pq só tem um aluno com um conjunto de 3 notas. Se tivesse mais alunos- esse loop ia printar todos os alunos.
        print(f"Aluno: {chave}")
        print(f"Notas: {valor}")
    print(f"Media: {media:.2f}")
    print(f"Situacão: {situacao}")


# Programa principal
def main():
    alunos = obter_notas()
    media = calcular_media(alunos)
    situacao = situacao_academica(media)
    exibir_relatorio(alunos, media, situacao)
    print("Fim do programa")

    
if __name__ == "__main__":
    main()

