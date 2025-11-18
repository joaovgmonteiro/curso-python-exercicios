# ex10) Dado o dicionário notas = {"João": 8.5, "Maria": 9.0, "Pedro": 7.5}, imprima o nome do aluno com a maior nota.

notas = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 7.5
}

comparador = 0
for chave, valor in notas.items():
    if valor > comparador:
        comparador = valor
        aluno_maior_nota = chave

print(f"O aluno/a com maior nota é {aluno_maior_nota} | Nota: {comparador}")

 