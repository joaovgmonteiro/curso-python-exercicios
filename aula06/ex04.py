"""
ex04) Com a estrutura WHILE, mostre os números múltiplos de 5 entre 0 e 50 na tela.
"""

i = 0
while i <= 50:
    if (i % 5 == 0):  # Múltiplos de 5
        print(i)
    i += 1