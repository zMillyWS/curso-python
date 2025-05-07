"""
Exercício 43: Calcule o preço à vista com desconto,
o valor parcelado e a comissão do vendedor.
"""
produto = input('Digite o valor do produto: ')
descontado = int(produto) - (int(produto) / 100 * 10)
parcela = int(produto) / 3
comissaoa = descontado / 100 * 5
comissaop = int(produto) / 100 * 5
print(f'O total a pagar a vista com desconto é R${descontado:.2f} '
      f'\nO valor parcelado em 3x sem juros é R${parcela:.2f}) '
      f'\nA comissao do vendedor, caso seja venda a vista é R${comissaoa:.2f}'
      f'\nA comissao do vendedor, no caso seja parcelada é R${comissaop:.2f}')
