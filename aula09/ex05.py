<<<<<<< HEAD
'''
Peça o nome de uma chave e tente buscá-la em um dicionário. Se a chave não existir, mostre uma mensagem.
alunos = {"Ana": 8.5, "Bruno":7.0, "Carlos":9.2}
'''

'''
minha versão
alunos = {"Ana":8.5, "Bruno":7.0, "Carlos":9.2}
try:
    nome_aluno = input("Digite o nome do aluno para descobrir sua nota: ")
    for chave, valor in alunos.items():
        if nome_aluno == chave:
            print(f"Nome: {chave} | Nota: {valor}")
except ValueError:
    print("erro")
except NameError:
    print("erro")
'''


def buscar_nomes():
    alunos = {
        "Ana": 8.5,
        "Bruno": 7.0,
        "Carlos": 9.2
    }
    try:
        nome = input("Nome: ").capitalize() # Transforma a primeira letra em caixa alta.
        nota = alunos[nome]
    except KeyError:
        print("Nome não encontrado.")
    else:
        print("O nome encontrado foi: ", nome)
        print(f"Aluno: {nome} | Nota: {nota}")
    finally:
        print("FIM")

=======
'''
Peça o nome de uma chave e tente buscá-la em um dicionário. Se a chave não existir, mostre uma mensagem.
alunos = {"Ana": 8.5, "Bruno":7.0, "Carlos":9.2}
'''

'''
minha versão
alunos = {"Ana":8.5, "Bruno":7.0, "Carlos":9.2}
try:
    nome_aluno = input("Digite o nome do aluno para descobrir sua nota: ")
    for chave, valor in alunos.items():
        if nome_aluno == chave:
            print(f"Nome: {chave} | Nota: {valor}")
except ValueError:
    print("erro")
except NameError:
    print("erro")
'''


def buscar_nomes():
    alunos = {
        "Ana": 8.5,
        "Bruno": 7.0,
        "Carlos": 9.2
    }
    try:
        nome = input("Nome: ").capitalize() # Transforma a primeira letra em caixa alta.
        nota = alunos[nome]
    except KeyError:
        print("Nome não encontrado.")
    else:
        print("O nome encontrado foi: ", nome)
        print(f"Aluno: {nome} | Nota: {nota}")
    finally:
        print("FIM")

>>>>>>> c805b8ce5dc597c03c8b6b2c09b995650e6437b7
buscar_nomes()