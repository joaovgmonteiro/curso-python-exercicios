def dividir(a: float, b: float) -> float:
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("Erro: dividido por zero.")
    else:
        print(f"Resultado da divisão: {resultado}")
    finally:
        print("Operação realizada!")

print("Programa Principal")
# Entrada de dados
try:
    num1 = float(input("Digite o numerador: "))
    num2 = float(input("Digite o denominador: "))

    dividir(num1, num2)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
except ValueError as erro:
    print("Erro: ", erro)
    