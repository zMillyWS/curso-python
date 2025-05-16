"""
3. Faça um programa que tenha uma função que receba uma
lista de inteiros e retorne o maior valor.
"""


import random


def maior_valor(lista: list[int]) -> int:
    """
    Função que recebe uma lista de inteiros e retorna o maior valor.

    :param lista: Lista de inteiros.
    :return: Maior valor da lista.
    """
    return max(lista)


# Testando a função
numeros = random.sample(range(1, 100), 10)
resultado = maior_valor(numeros)
print(f"O maior valor da lista {numeros} é {resultado}.")
