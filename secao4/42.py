"""
Exercício 42: Calcule o salário líquido de um funcionário com desconto de 2%.
"""
salariob = input('Digite o salário base do funcionario: ')
salarioi = int(salariob) - (int(salariob) / 100 * 2)
print(f'O salario total desse funcionario é R${salarioi:.2f}')
