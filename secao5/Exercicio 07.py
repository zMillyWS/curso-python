"""
Exercicio 07 Secao - 05

7. Faca um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais"
"""
num1, num2 = [int(x) for x in input("Digite dois números: ").split()]
if num1 > num2:
    print(f"O número {num1} é maior que {num2}")
elif num1 < num2:
    print(f"O número {num2} é maior que {num1}")
else:
    print(f"Os números são iguais")
