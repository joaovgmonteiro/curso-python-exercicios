<<<<<<< HEAD
'''
implemente a estrutura de repetição while no exercício 04 (Calculadora) para permitir 
que o usuário continue utilizando a calculador

'''

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1/n2

def calculadora():
    while True:
        try:
            print("Calculadora")
            numero1 = float(input("Digite o 1º número: "))
            numero2 = float(input("Digite o 2º número: "))

            print("+ Adição\n- Subtração\nX Multiplicação\n/ Divisão")
            op = input("Escolha operação que deseja realizar: ").upper()

            match op:
                case "+":
                    resultado = (f"{numero1} + {numero2} = {adicao(numero1, numero2)}")
                case "-":
                    resultado = (f"{numero1} - {numero2} = {subtracao(numero1, numero2)}")
                case "X":
                    resultado (f"{numero1} X {numero2} = {multiplicar(numero1, numero2)}")
                case "/":
                    resultado = (f"{numero1} / {numero2} = {dividir(numero1, numero2)}")
                case _:
                    resultado = ("Opção inválida.")
        except ValueError:
            print("Erro: valor não numérico digitado.")
        except ZeroDivisionError:
            print("Erro: dividido por zero.")
        else:
            print(resultado)
        finally:
            print("Operação realizada!")
        continuar = input("Deseja continuar no programa s/n ?")
        if continuar in ["s", "sim", "Sim", "SIM"]:
            continue
        else:
            break
        
    print("Calculadora Finalizada!")
            

# Programa principal
def main():
    calculadora() 

if __name__ == "__main__":
=======
'''
implemente a estrutura de repetição while no exercício 04 (Calculadora) para permitir 
que o usuário continue utilizando a calculador

'''

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1/n2

def calculadora():
    while True:
        try:
            print("Calculadora")
            numero1 = float(input("Digite o 1º número: "))
            numero2 = float(input("Digite o 2º número: "))

            print("+ Adição\n- Subtração\nX Multiplicação\n/ Divisão")
            op = input("Escolha operação que deseja realizar: ").upper()

            match op:
                case "+":
                    resultado = (f"{numero1} + {numero2} = {adicao(numero1, numero2)}")
                case "-":
                    resultado = (f"{numero1} - {numero2} = {subtracao(numero1, numero2)}")
                case "X":
                    resultado (f"{numero1} X {numero2} = {multiplicar(numero1, numero2)}")
                case "/":
                    resultado = (f"{numero1} / {numero2} = {dividir(numero1, numero2)}")
                case _:
                    resultado = ("Opção inválida.")
        except ValueError:
            print("Erro: valor não numérico digitado.")
        except ZeroDivisionError:
            print("Erro: dividido por zero.")
        else:
            print(resultado)
        finally:
            print("Operação realizada!")
        continuar = input("Deseja continuar no programa s/n ?")
        if continuar in ["s", "sim", "Sim", "SIM"]:
            continue
        else:
            break
        
    print("Calculadora Finalizada!")
            

# Programa principal
def main():
    calculadora() 

if __name__ == "__main__":
>>>>>>> c805b8ce5dc597c03c8b6b2c09b995650e6437b7
    main()