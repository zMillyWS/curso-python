"""
Exercício 44: Calcule o número de degraus
necessários para atingir uma altura desejada.
"""
a, b = input("Qual a altura do degrau e a "
             "altura que deseja alcancar?").split()
degraus = int(b) / int(a)
print(f'Para atingir a altura desejada voce deverá subir {
    int(degraus)} degraus.')
