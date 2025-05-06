"""
Exercicio 27 Secao - 05

27. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
5 a 7 anos: Infantil A
8 a 10: Infantil B
11 a 13: Juvenil A
14 a 17: Juvenil B
Maiores de 18: Sênior
"""
idade = input("Digite a idade do nadador:\n")
while not idade.isdigit():
    print("Por favor digite apenas números inteiros.")
    idade = input("Digite a idade do nadador:\n")
idade = int(idade)
if idade >= 5 and idade <= 7:
    print("Este nadador é Infantil A.")
elif idade >= 8 and idade <= 10:
    print("Este nadador é Infantil B.")
elif idade >= 11 and idade <= 13:
    print("Este jogador é Juvenil A.")
elif idade >= 14 and idade <= 17:
    print("Este nadador é Juvenil B.")
elif idade >= 18:
    print("Este nadador é Sênior.")
else:
    print("Idade abaixo de 5 anos não possui categoria.")
