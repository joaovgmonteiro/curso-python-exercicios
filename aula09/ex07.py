'''
Crie um programa que peça o nome e a idade de uma pessoa. Se o valor 
digitado para idade não for um número inteiro positivo, mostre uma 
mensagem de erro. Use try, except, else e finally para garantir o 
encerramento correto do programa:
'''
def validar_idade(idade):
    if idade <= 0:
        raise ValueError("Idade precisa ser um número maior que zero.")
    
def ler_idade():
    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        validar_idade(idade)
    except ValueError as err:
        print(f"Erro: {err}")
    else:
        print(f"Nome: {nome} | Idade: {idade}")
    finally:
        print("Operação realizada!")

ler_idade()