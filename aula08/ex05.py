'''
ex05) Classificar faixa etária
idade < 13 = "Criança"
idade < 18 = "Adolescente"
idade < 60 = "Adulto"
idade >= 60 = "Melhor idade"

'''

def classificar_faixa_etaria(idade: int) -> str:
    if idade < 13:
        faixa = "Criança"
    elif idade < 18:
        faixa = "Adolescente"
    elif idade < 60:
        faixa = "Adulto"
    else: 
        faixa = "Melhor idade"
    return faixa

idade_pessoa = int(input("Digite a idade: "))
faixa_etaria = classificar_faixa_etaria(idade_pessoa)

print(f"idade: {idade_pessoa} | Faixa etária: {faixa_etaria}")
