'''
Escreva um algoritmo em Python que leia uma opção escolhida pelo usuário e faça as seguintes rotinas:
1- Escolha um número e diga se é par ou ímpar
2- escolha dois valores e diga quem é o maior entre eles ou se são iguais
3- escolha um valor e calcule o dobro mostrando para o usuário o resultado.
'''
# continue - pula para a próxima iteração do loop

while True:
    print(15* "=")
    print("1-Par/Ímpar \n2-Maior/Menor \n3-Calcular dobro ")

    # Tratamento da escolha da opção
    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: Por favor, digite um número válido.")
        continue

    match op:
        case 1: # Par/impar
            num = int(input("Digite um número para verficar se é Par ou Ímpar: "))
            if (num % 2 == 0):
                sit = "par"
            else:
                sit = "ímpar"
            print(f"O número {num} é {sit}")
        case 2: # Maior entre números
            print("Digite dois números para descobrir o maior entre eles:")
            n1 = float(input("1º número: "))
            n2 = float(input("2º número: "))
            if (n1 == n2):
                print(f"{n1} = {n2}")
            elif (n1 > n2):
                print(f"{n1} > {n2}")
            else:
                print(f"{n2} > {n1}")
        case 3: # Calcular o dobro
            n3 = float(input("Digite um número para calcular o dobro: "))
            dobro = n3 * 2
            print(f"O dobro de {n3} = {dobro}")
        case _:
            print("Opção Inválida")
    cont = input("Você quer continuar o programa s/n ?")
    if cont == "n":
        break

# O print ocorre quando sai do loop, ou seja, quando o programa é finalizado (O usuário digita n).
print("Programa finalizado!")   

        