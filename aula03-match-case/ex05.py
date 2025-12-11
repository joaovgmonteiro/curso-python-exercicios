'''
Ex05) Receba dois números e um símbolo de operação (+, -, *, /)
'''

print("=" * 10, "CALCULADORA" , "="* 10)
n1 = float(input("Digite o 1º número: "))
op = input("Escolha uma operação para realizar com os números (+, -, *, /):")
n2 = float(input("Digite o 2º número: "))

match op:
    case "+":
        print("Operação escolhida: SOMA")
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
    case "-":
        print("Operação escolhida: SUBTRAÇÃO")
        sub = n1 - n2
        print(f"{n1} - {n2} = {sub}")
    case "*":
        print("Operação escolhida: MULTIPLICAÇÃO")
        mult = n1 * n2
        print(f"{n1} * {n2} = {mult}")
    case "/":
        print("Operação escolhida: DIVISÃO")
        div = n1 / n2
        print(f"{n1} : {n2} = {div}")
    case _:
        print("Operação incorreta!")



