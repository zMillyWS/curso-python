"""
Exercicio 16 Secao - 05

16. Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente.
"""
mes = ("Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
num = int(input("Digite um número de 1 á 12: "))
if num < 1 or num > 12:
    print("Número inválido")
else:
    print(f"Este número equivalente ao mes do ano é: {mes[num - 1]}")
