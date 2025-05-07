"""
Exercício 41: Calcule o salário mensal de um funcionário com um acréscimo de 10%.
"""
valor, horas = input(
    "Digite o valor da hora de trabalhado e o numero de horas trabalhadas no mês: "
).split()
salario = int(valor) * int(horas)
total = salario + (salario / 100 * 10)
print(f"O valor do mês a ser pago ao funcionario é de R${total:.2f}")
