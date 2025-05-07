"""
Exercício 40: Calcule o salário líquido de um encanador, descontando 8% de impostos.
"""
dias = int(input("Digite o número de dias que o encanador vai trabalhar: "))
salariob = dias * 30
salariol = salariob - (salariob / 100 * 8)
print(f"O salario liquido do encanador é R${salariol:.2f}")
