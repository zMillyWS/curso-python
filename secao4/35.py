"""
Exercício 35: Calcule a hipotenusa de um triângulo retângulo dados os catetos.
"""
a, b = input('Digite dois valores: ').split()
conta = int(a) ** 2 + int(b) ** 2
print(f'Se os catetos de um triangulo forem {a} e {b}, a hipotenusa é {conta}')
