'''
Ex07) O usuário digita a idade e o esporte é classificado dentro de um case:
Categorias:

1-Natação
idade < 10 = "Categoria: Mirim"
idade <= 14 = "Categoria: Infantil"
idade >14 "Categoria: Juvenil"

2-Corrida
idade < 16 = "Categoria: Júnior"
Idade >= 16 = "Categoria: Adulto"

3-Ciclismo
idade >= 18 = Categoria: Profissional"
idade <18 = "Categoria: Amador"
'''


idade = int(input("idade: "))
op = int(input("Escolha um esporte: 1-Natação 2-Corrida 3-Ciclismo: "))

match op:
    case _ if idade <= 0:
        esp = "Inválido"
        categoria = "Idade inválida."
    case 1: # Natação
        esp = "Natação"
        match idade:
            case _ if idade < 10:
                categoria = "MIRIM"
            case _ if idade <= 14:
                categoria = "INFANTIL"
            case _:
                categoria = "JUVENIL"
    case 2: # Corrida
        esp = "Corrida"
        match idade:
            case _ if idade < 16:
                categoria = "JÚNIOR"
            case _:
                categoria = "ADULTO"
            
    case 3: # Ciclismo
        esp = "Ciclismo"
        match idade:
            case _ if idade >= 18:
                categoria = "PROFISSIONAL"
            case _:
                categoria = "AMADOR"

    case _:
        esp = "Inválido"
        categoria  = "Categoria Inválida"

print(f"Idade: {idade} | Esporte: {esp} | Categoria: {categoria}")