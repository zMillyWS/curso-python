"""
Exercicio 30 Secao - 05

30. Faca um programa que receba três números e mostre-os em ordem crescente.
"""
a, b, c = input("Digite três números:\n").split()
while a.isalpha() or b.isalpha() or c.isalpha():
    print("Por favor, digite apenas números.")
    a, b, c = input("Digite três números:\n").split()
a = float(a)
b = float(b)
c = float(c)
lista = [a, b, c]
print(sorted(lista))
