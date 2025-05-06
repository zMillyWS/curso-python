"""
Exercicio 20 Secao - 05

20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo,
e, se forem, se é um triângulo escaleno, equilátero ou isóscele.
"""
a, b, c = input("Digite três valores: ").split()
while a.isalpha() or b.isalpha() or c.isalpha():
    print("Digite apenas números, por favor.")
    a, b, c = input("Digite três valores: ").split()
a = int(a)
b = int(b)
c = int(c)
if a + b < c or a + c < b or b + c < a:
    print("Estes não podem ser valores dos lados de um triângulo.")
elif a == b == c:
    print("Estes são valores dos lados de um triângulo equilátero.")
elif a == b or a == c or b == c:
    print("Estes são valores dos lados de um triângulo isósceles.")
else:
    print("Estes são valores dos lados de um triângulo escaleno.")
