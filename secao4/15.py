"""
Exercício 15: Converta um ângulo de radianos para graus.
"""
import math

radianos = float(input("Digite o ângulo em radianos: "))
graus = math.degrees(radianos)
print(f"O ângulo em graus é: {graus:.2f}")

R = 3.14
print(f'{R} radianos é igual à {round(R * 180 / 3.14)} graus')
