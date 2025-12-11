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
        print("Operação realizada!")