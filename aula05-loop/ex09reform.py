# Função Par/Impar.
def par_impar():
    try:
        num = int(input("Digite um número para verficar se é Par ou Ímpar: "))
        if (num % 2 == 0):
            sit = "par"
        else:
            sit = "ímpar"
        print(f"O número {num} é {sit}")
    except ValueError:
        print("Erro: Digitou um número inteiro inválido.")

# Função para descobrir o maior entre dois números.
def maior_numero():
    print("Digite dois números para descobrir o maior entre eles:")

    try:
        n1 = float(input("1º número: "))
        n2 = float(input("2º número: "))
        if (n1 == n2):
            print(f"{n1} = {n2}")
        elif (n1 > n2):
            print(f"{n1} > {n2}")
        else:
            print(f"{n2} > {n1}")
    except ValueError:
        print("Erro: Digitou um número inteiro inválido.")

# Função para calcular o dobro de um número.
def dobro_numero():
    try:
        n3 = float(input("Digite um número para calcular o dobro: "))
        dobro = n3 * 2
        print(f"O dobro de {n3} = {dobro}")
    except ValueError:
        print("Erro: Digitou um número inteiro inválido.")


# Programa principal
while True:
    print(15* "=")
    print("1-Par/Ímpar \n2-Maior/Menor \n3-Calcular dobro \n0-Sair ")

    # Tratamento da escolha da opção
    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: Por favor, digite um número válido.")
        continue    

    match op:
        case 0:
            print("Programa finalizado!")
            break
        case 1:
            par_impar()
        case 2:
            maior_numero()
        case 3:
            dobro_numero()
        case _:
            print("Opção Inválida")

    cont = input("Você quer continuar o programa s/n ?").lower().strip() # O strip remove espaços em branco 
    if cont in ['n', 'não', 'nao']:
        print("Programa finalizado!") 
        break
    elif cont not in ['s', 'sim']:
        print("Opção inválida! Continuando...")


 """
if __name__ == "__main__":      Se o arquivo que estiver sendo executado for o principal o nome dele vai ser __main__ e ele vai chamar a função e executar main.
    main()                      mas se o arquivo estiver sendo importado para outro programa ele não vai realizar essa execução. É útil usar pela facilidade de reusar em
                                outros programa com import ex09reform.py
 """                                