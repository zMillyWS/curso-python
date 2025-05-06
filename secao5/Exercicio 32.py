"""
Exercicio 32 Secao - 05

32. Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete, e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche.
"""


def cardapio(codigo):
    opcoes = {
        "100": f"Você escolheu {quant} Cachorro(s) Quente(s), o valor total será de R${1.20 * quant:.2f}",
        "101": f"Você escolheu {quant} Bauru(s) Simples, o valor total será de R${1.30 * quant:.2f}",
        "102": f"Você escolheu {quant} Bauru(s) com Ovo(s), o valor total será R${1.50 * quant:.2f}",
        "103": f"Você escolheu {quant} Hamburguer(s), o valor total será R${1.20 * quant:.2f}",
        "104": f"Você escolheu {quant} Cheeseburguer(s), o valor total será R${1.70 * quant:.2f}",
        "105": f"Você escolheu {quant} Suco(s), o valor total será R${2.20 * quant:.2f}",
        "106": f"Você escolheu {quant} Refrigerante(s), o valor total será R${quant:.2f}"
    }
    return opcoes.get(codigo, "Código inexistente.")


codigo = input("Digite o código do produto:\n")
while not codigo.isdigit():
    print("Por favor digite apenas caracteres numéricos inteiros.")
    codigo = input("Digite o código do produto:\n")
quant = input("Digite a quantidade que deseja:\n")
while not quant.isdigit():
    print("Por favor digite apenas caracteres numéricos inteiros.")
    quant = input("Digite a quantidade que deseja:\n")
quant = int(quant)
print(cardapio(codigo))
