"""
Exercicio 03 Secao - 05

3. Leia um número real. Se o número for positivo, imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""
numeroR = int(input('Digite um número:'))
if numeroR >= 0:
    raiz2 = numeroR ** 0.5
    print(f'A raiz quadrada de {numeroR} é {raiz2:.2f}')
else:
    quadrado = numeroR ** 2
    print(f'{numeroR} ao quadrado é {quadrado:.2f}')