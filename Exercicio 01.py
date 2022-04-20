"""
Exercicio 01 Secao - 05

1. Faca um programa que receba dois números e mostre qual deles é o maior.
"""
a, b = [float(x) for x in input('Digite dois números:').split()]
if a < b:
    print(f'{b} é maior que {a}')
elif a > b:
    print(f'{a} é maior que {b}')
else:
    print(f'{a} e {b} são de valores iguais')
