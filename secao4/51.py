"""
Exercício 51: Divida um prêmio entre três
amigos proporcionalmente ao valor investido por cada um.
"""
amg1, amg2, amg3 = input("Digite o nome dos três amigos: ").split()

invest1 = float(input(f"Digite o valor que o {amg1.title()} investiu: R$"))
invest2 = float(input(f"Digite o valor que o {amg2.title()} investiu: R$"))
invest3 = float(input(f"Digite o valor que o {amg3.title()} investiu: R$"))

premio = float(input("Digite o valor do premio: R$"))

soma = premio / (invest1 + invest2 + invest3)
premio_1 = soma * invest1
premio_2 = soma * invest2
premio_3 = soma * invest3

print(f"Para o valor do premio ser dividido igualmente"
      f"de acordo com o investimento de cada um,\n"
      f" {amg1.title()} deverá receber R${premio_1:.2f},"
      f" {amg2.title()} deverá receber R${premio_2:.2f}"
      f"e {amg3.title()} deverá receber R${premio_3:.2f}")
