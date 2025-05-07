"""
Exercício 28: Leia três números inteiros e exiba a soma dos quadrados deles.
"""
a, b, c = [int(numero) for numero in input("Digite três números: ").split()]
print(
    f"A soma dos quadrados desses números é {(a ** 2) + (b ** 2) + (c ** 2)}")
