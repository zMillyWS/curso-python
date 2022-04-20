"""
Exercicio 02 Secao - 05

2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número ofr negativo, mostre uma mensagem dizendo que o número é inválido.
"""
numero = int(input('Digite um numero:'))
if numero >= 0:
    raiz = numero ** 0.5
    print(f'A raiz quadrada de {numero} é {raiz}')
else:
    print('Número é invalido')
