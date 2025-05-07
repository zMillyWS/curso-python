"""
Exercício 37: Calcule o preço de um produto com desconto de 12%.
"""
valor = int(input('Digite o valor do produto:'))
desconto = valor / 100 * 12
print(
    f'Com desconto de 12% esse produto de R${valor:.2f} fica apenas R${valor - desconto:.2f}')
