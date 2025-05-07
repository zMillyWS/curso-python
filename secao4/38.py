"""
Exercício 38: Calcule o novo salário com um aumento de 25%.
"""
salario = int(input('Digite o valor do seu salario:'))
aumento = salario / 100 * 25
print(
    f'Você recebeu um aumento de 25% e seu salario foi de R${salario:.2f} para R${salario + aumento:.2f}')
