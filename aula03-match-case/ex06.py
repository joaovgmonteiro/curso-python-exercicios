'''
ex06)   Informe uma categoria conforme a idade:
        idade < 12
            criança
        idade < 18
            Adolescente
        idade < 60
            Adulto
        idade > 60
            Melhor idade
'''

idade = int(input("Idade: "))

match idade:
    case _ if idade <= 0:
        print("Opção inválida!")
    case _ if idade < 12:
        print("Criança")
    case _ if idade < 18:
        print("Adolescente")
    case _ if idade < 60:
        print("Adulto")
    case _: # Qualquer valor >= 60 válido
        print("Melhor idade")