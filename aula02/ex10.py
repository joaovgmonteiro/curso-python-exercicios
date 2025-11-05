'''
Leia a idade de uma pessoa e informe:
• “Criança” se menor que 12
• “Adolescente” se entre 12 e 17
• “Adulto” se entre 18 e 59
• “Idoso” se 60 ou mais

'''

idade = int(input("Digite a idade: "))


if (idade >0 and idade < 12):
    clas = "Criança"
elif (idade >= 12 and idade <= 17):
    clas = "Adolescente"
elif (idade >= 18 and idade <= 59):
    clas = "Adulto"
else: 
    clas = "Idoso"

print("Essa pessoa é", clas)