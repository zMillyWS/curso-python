"""
Exercicio 11 Secao - 05

11. Escreva um programa que leia um número intiero maior que zero e
devolva a soma de todos os seus algarismos.
"""
num = input("Digite um número: ")
lista = list(num)
intlista = map(int, num)
soma = sum(num)
if int(num) >= 0:
    print(f"A soma dos números é: {soma}")
else:
    print("Número inválido")
