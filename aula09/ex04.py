# Leia duas notas, calcule a média e trate erros de entrada (valor inválido ou divisão incorreta)

def calcular_media():
    try:
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        media = (nota1 + nota2)/2
    except ValueError:
        print("Erro: valor não numérico")
    else:        
        print(f"A média das notas: {media}")
    finally:
        print("Operação realizada!")

# Programa principal
calcular_media()
