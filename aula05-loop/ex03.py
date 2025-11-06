# Mostrar os números pares entre 0 e 100.
cont = 0
for i in range (0,101):
    if (i % 2 == 0):
        print(i)
        cont = cont + 1

print("A quantidade de números pares no intervalo [0 e 100]: ", cont)
