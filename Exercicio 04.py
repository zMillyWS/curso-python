"""
Exercicio 04 Secao - 05

4. Faca um programa que leia um número e, caso ele seja positivo, calcule e mostre:
   - O número digitado ao quadrado
   - A raiz quadrada do número digitado
"""
num = int(input('Digite um número:'))
if num >= 0:
    qua = num ** 2
    print(f'{num} ao quadrado é {qua}')
    ra = num ** 0.5
    print(f'A raiz quadrada de {num} é {ra:.2f}')
