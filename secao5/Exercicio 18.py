"""
Exercicio 18 Secao - 05

18. Faca um programa que mostre ao usuário um menu com 4 opcoes de operacões matemáticas.
O usuário escolhe uma das opcoes, e o seu programa pede dois valores numéricos e realiza a operacão.
"""
menu = input("Escolha uma operacão:\n [1] Adicão\n [2] Subtracão\n [3] Divisão\n [4] Multiplicacão\n = ")
while menu.isalpha() or int(menu) < 1 or int(menu) > 4:
    print("Valor inválido, por favor insira um número entre 1 e 4.")
    menu = input("Escolha uma operacão:\n [1] Adicão\n [2] Subtracão\n [3] Divisão\n [4] Multiplicacão\n = ")
num1 = (input("Digite o primeiro número: "))
num2 = (input("Digite o segundo número: "))
while num1.isalpha() or num2.isalpha():
    print("Digite apenas caracteres numéricos, por favor.")
    num1 = (input("Digite o primeiro número: "))
    num2 = (input("Digite o segundo número: "))
num1 = float(num1)
num2 = float(num2)
if int(menu) == 1:
    adicao = num1 + num2
    print(f"A operacão escolhida foi Adicão:\n {num1} + {num2} = {adicao}")
elif int(menu) == 2:
    sub = num1 - num2
    print(f"A operacão escolhida foi Subtracão:\n {num1} - {num2} = {sub}")
elif int(menu) == 3:
    div = num1 / num2
    print(f"A operacão escolhida foi Divisão:\n {num1} / {num2} = {div:.2f}")
elif int(menu) == 4:
    mult = num1 * num2
    print(f"A operacão escolhida foi Multiplicacão:\n {num1} x {num2} = {mult}")
else:
    print("Valores inválidos, tente novamente.")
