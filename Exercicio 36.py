"""
Exercicio 36 Secao - 05

36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
"""
venda = input("Qual o valor da venda mensal? \nR$")
while venda.isalpha():
    print("Por favor digite apenas caracteres numéricos.")
    venda = input("Qual o valor da venda? \nR$")
venda = float(venda)
if venda >= 100_000:
    comissao = (venda / 100 * 16) + 700
else:
    porcent = venda / 100 * 14
    if 80_000 <= venda < 100_000:
        comissao = porcent + 650
    elif 60_000 <= venda < 80_000:
        comissao = porcent + 600
    elif 40_000 <= venda < 60_000:
        comissao = porcent + 550
    elif 20_000 <= venda < 40_000:
        comissao = porcent + 500
    elif venda < 20_000:
        comissao = porcent + 400
print(f"A comissão que deve ser paga ao vendedor é de R${comissao:.2f}")
