'''
ex09) Crie um programa em python que utilize funções para analisar uma lista de números inteiros fornecidos pelo usuário. O programa deve:
Ler 10 números inteiros, inseridos pelo usuário, armazenando-os em uma lista.
Implementar as seguintes funções:

'''

def maior_valor(lista):
    return max(lista)

def menor_valor(lista):
    return min(lista)

def tamanho_lista(lista):
    return len(lista)

def main():
    numeros = []

    print("Digite 10 números inteiros: ")
    for i in range(1,10):
        num  = int(input(f"Digite o {i}º número: "))
        numeros.append(num)
    
    print("\nLista digitada: ", numeros)
    print("Maior valor: ", maior_valor(numeros))
    print("Menor valor: ", menor_valor(numeros))
    print("Tamanho da lisa: ", tamanho_lista(numeros))


if __name__ == "__main__":
    main()