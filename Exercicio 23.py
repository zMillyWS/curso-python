"""
Exercicio 23 Secao - 05

23. Determine se um determinado ano lido é bissexto.
"""
ano = input("Digite o ano: ")
while not ano.isdigit():
    print("Valor inválido. Por favor digite apenas caracteres numéricos inteiros.")
    ano = input("Digite o ano: ")
ano = int(ano)
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        print("O ano é bissexto.")
    else:
        print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
