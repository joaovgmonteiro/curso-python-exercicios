<<<<<<< HEAD
'''
Crie um programa que leia um número digitado pelo usuário e converta para int. Se o valor não for númerico, mostre uma mensagem de erro.
'''

def ler_inteiro():
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Erro: valor não numérico ")
    else:
        print(f"Número digitado: {numero}")
    finally:
=======
'''
Crie um programa que leia um número digitado pelo usuário e converta para int. Se o valor não for númerico, mostre uma mensagem de erro.
'''

def ler_inteiro():
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Erro: valor não numérico ")
    else:
        print(f"Número digitado: {numero}")
    finally:
>>>>>>> c805b8ce5dc597c03c8b6b2c09b995650e6437b7
        print("Operação realizada!")