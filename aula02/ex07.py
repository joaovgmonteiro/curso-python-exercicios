# Ex07) Peça um número e informe se ele é positivo, negativo ou zero.

num = float(input("Informe um número: "))
if (num == 0):
    s = "igual a 0."
elif (num > 0):
    s = "POSITIVO"
else:
    s = "NEGATIVO"

print(f"O valor digitado é {s}")