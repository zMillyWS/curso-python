"""
Exercicio 40 Secao - 05

40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
A comissão e os impostos são calculados sobre o custo da fábrica.
Leia o custo de fábrica e escreva o custo ao consumidor.
"""
# Recebendo e declarando variáveis
imposto = 0
fabrica = input("Digite o preco do carro do custo de fábrica:\n")

# Verificando se o valor é numérico
while not fabrica.isdigit():
    print("Por favor, utilize apenas caracteres numéricos.")
    fabrica = input("Digite o preco do carro do custo de fábrica:\n")

fabrica = float(fabrica)

# Calculando a quantidade de imposto e comissao
if fabrica <= 12000:
    comissao = fabrica / 100 * 5
elif 12000 <= fabrica <= 25000:
    comissao = fabrica / 100 * 10
    imposto = fabrica / 100 + 15
elif fabrica > 25000:
    comissao = fabrica / 100 * 15
    imposto = fabrica / 100 * 20

# Calculando custo total
total = fabrica + comissao + imposto

# Imprimindo resultado
print(f"O custo total do carro ao consumidor é de R${total:.2f}")
