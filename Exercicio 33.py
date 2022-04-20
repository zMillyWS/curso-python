"""
Exercicio 33 Secao - 05

33. Um produto vai sofrer aumento de acordo com a tabela abaixo.
Leia o preco antigo, calcule e escreva o preco novo.

Até R$50: 5%
Entre R$500 e R$100: 10%
Acima de R$100: 15%
"""
preco_ant = input("Digite o preco antigo: \nR$")
while preco_ant.isalpha():
    print("Por favor digite apenas caracteres numéricos.")
    preco_ant = input("Digite o preco antigo: \nR$")
preco_ant = float(preco_ant)
if preco_ant <= 50:
    preco_novo = (preco_ant / 100 * 5) + preco_ant
elif 50 < preco_ant <= 100:
    preco_novo = preco_ant + (preco_ant / 100 * 10)
else:
    preco_novo = preco_ant + (preco_ant / 100 * 15)
if preco_novo <= 80:
    print(f"O preco novo é R${preco_novo:.2f}, é um preco barato.")
elif 80 < preco_novo <= 120:
    print(f"O preco novo é R${preco_novo:.2f}, é um preco normal.")
elif 120 < preco_novo <= 200:
    print(f"O preco novo é R${preco_novo:.2f}, é um preco caro.")
else:
    print(f"O preco novo é R${preco_novo:.2f}, é um preco muito caro.")
