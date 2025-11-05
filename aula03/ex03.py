'''
Ex03) Solicite um número de 1 a 7 e mostre o dia correspondente da semana.

'''

dia = int(input("Escolha um número de 1 a 7 para saber qual o dia da semana: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case _:
        print("Você digitou um número incorreto.")