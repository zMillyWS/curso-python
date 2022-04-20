"""
Exercicio 25 Secao - 05

25. Calcule as raízes da equacão de segundo grau.
"""
import math
a = input("Digite o A da equacão: ")
b = input("Digite o B da equacão: ")
c = input("Digite o C da equacão: ")
while a.isalpha() or b.isalpha() or c.isalpha():
    print("Por favor, digite apenas números.")
    a = input("Digite o A da equacão: ")
    b = input("Digite o B da equacão: ")
    c = input("Digite o C da equacão: ")
a = float(a)
b = float(b)
c = float(c)
delta = b ** 2 + (-4 * a * c)
if delta < 0:
    print("O Delta é negativo portanto não tem raiz.")
elif delta == 0:
    x1 = (-b) + math.sqrt(delta) // (2 * a)
    print(f"A raiz da equacacão é única: x = {x1}")
else:
    x1 = (-b) + math.sqrt(delta) // (2 * a)
    x2 = (-b) - math.sqrt(delta) // (2 * a)
    print(f"As raizes da equacao são: x1 = {x1} e x2 = {x2}")
