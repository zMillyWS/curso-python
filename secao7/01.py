"""
1. Crie um programa que tenha uma função que
recebe um parâmetro inteiro e devolve o seu dobro.
"""


def dobro(numero: int) -> int:
    """
    Função que recebe um número inteiro e devolve o seu dobro.

    :param numero: Número inteiro a ser dobrado.
    :return: Dobro do número.
    """
    return numero * 2


# Testando a função
numero = int(input("Digite um número inteiro: "))
resultado = dobro(numero)
print(f"O dobro de {numero} é {resultado}.")
