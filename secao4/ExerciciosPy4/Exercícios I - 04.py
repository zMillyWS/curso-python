"""
Exercícios I Secao 04
"""

# 1.

numero = 10
print(numero)
print(type(numero))

# 2.
numero_r = 10.5
print(numero_r)
print(type(numero_r))

# 3.
a, b, c = input('Digite três valores: ').split()
print(f'Então, a soma de {a} , {b} e {c} é {int(a) + int(b) + int(c)}')

# 4.
numero_r2 = input('Informe um número para elevar ao quadrado:')
print(f'{numero_r2} elevado ao quadrado é {int(numero_r2) ** 2}')

# 5.
print(f'A quinta parte de {numero_r2} é {int(numero_r2) / 5}')

# 6.
C = 28
F = C*(9.0/5.0)+32.0
print(f'{C} graus Celsius é igual a {F:.2f} Fahrenheit')

# 7.
F2 = 82.4
C2 = 5.0 * (F - 32.0)/9.0
print(f'{F2} graus Fahrenheit é igual a {C2:.2f} graus Celsius')

# 8.
K = 301.15
C3 = K - 273.15
print(f'{K} graus Kelvin é igual à {C3:.2f} graus Celsius')

# 9.
C4 = 28
K2 = C + 273.15
print(f'{C4} graus Celsius é igual a {K2:.2f} graus Kelvin')

# 10.
K = 80
M = K/3.6
print(f'{K} km/h é igual à {M:.2f} m/s')
