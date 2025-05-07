"""
Exercício 36: Calcule o volume de um cilindro circular dado o raio e a altura.
"""
altura, raio = input(
    'Digite o valor da altura e do raio de um cilindro circular ').split()
v = 3.141592 * int(raio) ** 2 * int(altura)
print(f'O volume desse cilindro é {v:.2f}')
