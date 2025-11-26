'''
Crie um programa que utilize as funções para realizar a divisão entre dois números reais informados pelo usuário.
O programa deve:
1. Definir uma função chamada dividir(a, b) que receba dois valores numéricos como parâmetros.
2. Calcular e retornar o resultado da divisão do primeiro número (a) pelo segundo (b)
3. No programa principal, solicitar que o usuário digite o numerador e o denominador
4. Exibir na tela o resultado da divisão com uma mensagem explicativa.
Dica: Use o comando return dentro da função para devolver o valor da operação e exibí-lo fora dela.
'''


def dividir(a: float, b: float) -> float: 
    try:
        div = a/b
        return div
    except ZeroDivisionError:
        print("Erro: divisão por 0")
    
     


def main():
    try:
        numerador = float(input("Digite o numerador da divisão: "))
        denominador = float(input("Digite o denominador da divisão: "))
        resultado_divisao = dividir(numerador, denominador)
        print(f"Resultado da divisão: {numerador}/{denominador} = {resultado_divisao}")
    except ValueError as erro:
        print(f"Erro: {erro}")
    print("Programa finalizado")

if __name__ == "__main__":
    main()
    


