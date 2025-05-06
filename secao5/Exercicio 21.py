"""
Exercicio 21 Secao - 05

21. Escreva o menu de opcoes abaixo. Leia a opcão do usuário e execute a operacão escolhida.
Escreva uma mensagem de erro se a opcão for inválida.
"""
opcao = input("Escolha uma opcão:\n 1- Soma de 2 números.\n 2- Diferenca entre 2 números (maior pelo menor).\n "
              "3- Produto entre 2 números.\n 4- Divisão entre 2 números (o denominador não pode ser zero).\nOpcão: ")
while opcao.isalpha() or int(opcao) < 1 or int(opcao) > 4:
    print("Valor inválido. Por favor digite um número de 1 à 4.")
    opcao = input("Escolha uma opcão:\n 1- Soma de 2 números.\n 2- Diferenca entre 2 números (maior pelo menor).\n "
          "3- Produto entre 2 números.\n 4- Divisão entre 2 números (o denominador não pode ser zero).\nOpcão: ")
a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")
while a.isalpha() or b.isalpha():
    print("Valor inválido. Por favor, utilize apenas caracteres numéricos.")
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")
a = float(a)
b = float(b)
if int(opcao) == 1:
    print(f"A soma entre {a} e {b} é {a + b}.")
elif int(opcao) == 2:
    if a < b:
        print("O primeiro número deve ser maior do que o segundo. Por favor, tente novamente.")
    else:
        print(f"A diferenca entre {a} e {b} é {a - b}")
elif int(opcao) == 3:
    print(f"O produto entre {a} e {b} é {a * b}")
elif int(opcao) == 4:
    if b == 0:
        print("O denominador (segundo número) não pode ser zero")
    else:
        print(f"A divisão entre {a} e {b} é {a // b}")
