"""
Crie um programa que leia 10 números inteiros e armazene-os em uma lista. Em seguida, mostre os números pares da lista.
"""

lista = []
for indice in range(10):
    try:
        valor = int(input("Digite um valor inteiro: "))
        valor = int(input("Digite um valor inteiro: "))
        lista.append(valor)
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")
        break
    
for numero in lista:
    if numero % 2 == 0:
        print(numero)
