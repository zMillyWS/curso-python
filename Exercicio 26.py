"""
Exercicio 26 Secao - 05

26. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
calcule o consumo em Km/l e escreva uma mensagem de acordo.
"""
km = input("Digite a distância em Km:\n")
litros = input("Digite a quantidade de litros consumidos:\n")
while km.isalpha() or litros.isalpha():
    print("Por favor, digite apenas números.")
    km = input("Digite a distância em Km:\n")
    litros = input("Digite a quantidade de litros consumidos:\n")
km = float(km)
litros = float(litros)
kmpl = km // litros
if kmpl < 8:
    print("Venda o carro!")
elif kmpl > 8 and kmpl < 12:
    print("Econômico!")
else:
    print("Super econômico!")
