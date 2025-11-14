"""
Ex05) Crie um algoritmo em python que tenha a entrada de nome e salário bruto.
Com função, resolva as situações abaixo:
INSS
Se o salário bruto >= 1800 desconte 11%
Se o salário bruto < 1800 desconte 9%
Vale Transporte
Se o salário bruto >= 1500 desconte 6%
Se o salário bruto < 1500 desconte 5%
Bônus
Se o sb >= 1240 some com mais 700 reais
Se o sb < 1240 some com mais 500 reais
Cargo
Se o salário bruto >= 3000 = acionista
Se o sb >= 2000 = gerente
se o sb < 2000 = vendedor
Salario liquido:
Sl = Sb - (inss + vale) + bonus
"""

def calcular_inss(salario: float) -> float:
    if salario >= 1800:
        desconto = salario * 0.11
    else:
        desconto = salario * 0.09
    return desconto

def calcular_vale_transporte(salario: float) -> float:
    if salario >= 1500:
        desconto = salario * 0.06
    else:
        desconto = salario * 0.05
    return desconto

def calcular_bonus(salario: float) -> float:
    if salario >= 1240:
        acrescimo = 700
    else:
        acrescimo = 500
    return acrescimo

def determinar_cargo(salario: float) -> str:
    if salario >= 3000:
        oficio = "Acionista"
    elif salario >= 2000:
        oficio = "Gerente"
    else:
        oficio = "Vendedor"
    return oficio

def calcular_salario_liquido(salario: float, inss: float, vale: float, bonus: float) -> float:
    return salario - (inss + vale) + bonus

# Programa principal
def main():
    # Entrada de dados
    nome = input("Digite o seu nome: ")
    salario_bruto = float(input("Digite o salário bruto: "))

    if salario_bruto <= 0:
        print("Erro: Salário deve ser positivo!")
        return

    # INSS
    valor_inss = calcular_inss(salario_bruto)
    # vale transporte
    valor_vale_transporte = calcular_vale_transporte(salario_bruto)
    # bonus
    valor_bonus = calcular_bonus(salario_bruto)
    # Descobrir cargo
    tipo_cargo = determinar_cargo(salario_bruto)
    # Descobrir o salario liquido
    salario_liquido = calcular_salario_liquido(salario_bruto, valor_inss, valor_vale_transporte, valor_bonus)

    # Saída de dados
    print("="*20)
    print(f"Nome: {nome} | Cargo: {tipo_cargo.upper()} | Salário Bruto: R$ {salario_bruto}")
    print(f"INSS: - R$ {valor_inss:.2f} | Vale Transporte: - R$ {valor_vale_transporte:.2f}")
    print(f"Bonus: + R$ {valor_bonus}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")


if __name__ == "__main__":
    main()

