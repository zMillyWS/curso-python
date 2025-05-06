"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos.
"""

# Lê 6 valores inteiros do usuário
valores = []
for numero in range(6):
    try:
        valor = int(input("Digite um valor inteiro: "))
        valores.append(valor)
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")
        break
    

# Exibe os valores lidos
print("Valores lidos:", valores)