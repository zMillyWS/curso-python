"""
Exercicio 19 Secao - 05

19. Faca um programa para verificar se um determinado número inteiro é divisível por 3 ou 5.
"""
num = int(input("Digite um número: "))
if num % 3 == 0:
    div = num // 3
    print(f"Este número é divisível por 3, e o resultado de sua divisão é: {div}")
elif num % 5 == 0:
    div = num // 5
    print(f"Este número é divisível por 5, e o resultado de sua divisão é: {div}")
else:
    print("Este número não é divisível por 3 e nem por 5.")
