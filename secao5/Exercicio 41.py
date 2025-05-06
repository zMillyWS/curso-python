"""
Exercicio 41 Secao - 05

41. Faca um algoritmo que calcule o IMC de uma pessoa e mostre sua classificacão.
"""
# Recebendo e declarando variaveis
peso = input("Digite seu peso:\n")
altura = input("Digite sua altura:\n")

# Verificando se são números
while peso.isalpha() or altura.isalpha():
    print("Por favor digite apenas caracteres numéericos.")
    peso = input("Digite seu peso:\n")
    altura = input("Digite sua altura:\n")

# Calculando IMC
imc = float(peso) / (float(altura) ** 2)

# Classificando
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Saudável"
elif 25 <= imc < 30:
    classificacao = "Peso em excesso"
elif 30 <= imc < 35:
    classificacao = "Obesidade I"
elif 35 <= imc < 40:
    classificacao = "Obesidade II (severa)"
elif imc >= 40:
    classificacao = "Obesidade III (mórbida)"

# Imprimindo resultado
print(f"Sua classificacao é: \n{classificacao}")
