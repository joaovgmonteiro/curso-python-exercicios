# O usuário escolhe os números da lista vazia e a quantidade de vezes que testara o programa.

numeros = []
quantidade = int(input("Quantas vezes você quer testar? "))

for i in range(1, quantidade + 1):
    numero = int(input(f"Digite o {i}º número: "))
    nome = input(f"Digite o {i} nome: ")
    numeros.append(numero) # nome_da_lista.append(numero_adicionado) Insere um numero na lista numeros.
    numeros.append(nome)
print(f"Números digitados pelo usuário: {numeros}")


# Numero - Class
# numeros - Array-lista[] 
# numero -  objeto/variável 
            