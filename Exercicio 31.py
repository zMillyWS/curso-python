"""
Exercicio 31 Secao - 05

31. Faca um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir,
verifique e mostre qual a classificacão dessa pessoa.
"""
altura = input("Digite sua altura:\n")
peso = input("Digite seu peso:\n")
while altura.isalpha() or peso.isalpha():
    print("Por favor, digite apenas caracteres numéricos.")
    altura = input("Digite sua altura:\n")
    peso = input("Digite seu peso:\n")
altura = float(altura)
peso = float(peso)
if altura < 1.20:
    if peso <= 60:
        print("Sua classificacão é A.")
    elif 60 < peso <= 90:
        print("Sua classificacão é D.")
    else:
        print("Sua classificacão é G")
elif 1.20 < altura <= 1.70:
    if peso <= 60:
        print("Sua classificacão é B.")
    elif 60 < peso <= 90:
        print("Sua classificacão é E.")
    else:
        print("Sua classificacão é H")
else:
    if peso <= 60:
        print("Sua classificacão é C.")
    elif 60 < peso <= 90:
        print("Sua classificacão é F.")
    else:
        print("Sua classificacão é I")
