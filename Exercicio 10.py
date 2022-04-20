"""
Exercicio 10 Secao - 05

10. Faca um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas:
Homens: (72 * h) - 58
Mulheres (62,1 * h) - 44,7
"""
sexo = input("Qual seu sexo? ")
altura = float(input("Qual a sua altura? "))
if sexo == "feminino":
    ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {ideal:.1f}")
elif sexo == "masculino":
    ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {ideal:.1f}")
else:
    print("Sexo não é válido")
