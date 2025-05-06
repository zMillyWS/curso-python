"""
Exercicio 12 Secao - 05

12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido".
Se o número for positivo, calcular o logaritmo deste número.
"""
import math
num = float(input("Digite um número: "))
if num >= 10:
    log = math.log(num)
    print(f"O logarítimo desse número é: {log}")
else:
    print("Número inválido")
