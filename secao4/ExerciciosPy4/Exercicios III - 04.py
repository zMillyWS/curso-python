"""
Exercicios III - Secao 04.
"""
# 21.
L = 111.11
print(f'{L} libras é igual à {round(L * 0.45)} quilogramas')

# 22.
J = 100
print(f'{J} jardas é igual à {0.91 * J} metros')

# 23.
M = 91
print(f'{M} metros é igual à {M / 0.91} jardas')

# 24.
Mq = 5000
print(f'{Mq} metros quadrados é igual à {Mq * 0.000247:.4f} acres')

# 25.
A = 1.2350
print(f'{A} acres é igual à {round(A * 4048.58)} metros quadrados')

# 26.
M2 = 5000
print(f'{M2} metros quadrados é igual à {M2 * 0.0001} hectares')

# 27.
H = 0.5
print(f'{H} hectares é igual à {round(H * 10000)} metros quadrados')

# 28.
a, b, c = [int(numero) for numero in input('Digite três números:').split()]
print(f'A soma dos quadrados desses números é {(a ** 2) + (b ** 2) + (c ** 2)}')
print(a, b, c)

# 29.
prova = 10
prova2 = 7.5
prova3 = 5
prova4 = 9.5

print(f'A média foi de {(prova + prova2 + prova3 + prova4) / 4:.1f}')

# 30.
R = 50.00
print(f'R$:{R:.2f} equivalem à US$:{R / 5.6853:.2f}')
