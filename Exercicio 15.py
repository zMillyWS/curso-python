"""
Exercicio 15 Secao - 05

15. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente.
"""
num = int(input("Digite um número de 1 a 7: "))
semana = ("Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sábado")
if num < 1 or num > 7:
    print("Número inválido")
else:
    print(f"Este número equivale ao dia da semana é: {semana[num - 1]}")
