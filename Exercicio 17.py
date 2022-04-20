"""
Exercicio 17 Secao - 05

17. Faca um programa que calcule e mostre a área de um trapézio.
"""
basemaior = float(input("Digite a base maior do trapézio: "))
basemenor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))
if basemaior < 0 or basemenor < 0:
    print("Bases devem ser maior do que 0")
else:
    area = (basemaior + basemenor) * altura //  2
    print(f"A area desse trapézio é: {area}")
