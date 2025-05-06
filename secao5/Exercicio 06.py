"""
Exercicio 06 Secao - 05

6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferenca existente entre ambos.
"""
num1, num2 = [int(x) for x in input("Digite dois números: ").split()]
diferenca = num2 - num1
if num1 > num2:
    print(f"O número {num1} é maior que {num2}, e tem uma diferenca de {diferenca}")
elif num1 < num2:
    print(f"O número {num2} é maior que {num1}, e tem uma diferenca de {diferenca}")
else:
    print(f"Os números são iguais")