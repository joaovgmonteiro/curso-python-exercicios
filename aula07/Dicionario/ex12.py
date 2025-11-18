# Ex12) Crie um programa que conte quantas vezes cada palavra aparece em uma frase.

#split 

frase = "python é legal python é poderoso"
palavras = {}
frase_separada = frase.split()


for i in frase_separada: 
    if i not in palavras:
        palavras[i] = 1
    else:
        palavras[i] += 1
        
   
print(palavras.items())