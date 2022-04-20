"""
Exercicio 39 Secao - 05

39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o
salário atual e o tempo de servico de cada funcionário.
Faca um programa que leia:
- O valor do salário atual do funcionário;
- O tempo de servico desse funcionário na empresa (em anos).
"""
# Recebendo e declarando as variaveis
bonus = 0
aumento = 0
salario = input("Digite o salário atual do funcionário:\n")
tempo = input("Digite o tempo de servico (em anos) na empresa:\n")

# Verificando se os valores dados sao números
while not salario.isdigit() or not tempo.isdigit():
    print("Por favor, digite apenas caracteres numéricos.")
    salario = input("Digite o salário atual do funcionário:\n")
    tempo = input("Digite o tempo de servico (em anos) na empresa:\n")

# Transformando as variaveis em float e int
salario = float(salario)
tempo = int(tempo)

# Verificando a quatidade do bonus
if 1 <= tempo <= 3:
    bonus = 100
elif 4 <= tempo <= 6:
    bonus = 200
elif 7 <= tempo <= 10:
    bonus = 300
elif tempo > 10:
    bonus = 500

# Verificando a porcentagem de aumento de acordo com o salário
if salario <= 500:
    aumento = salario / 100 * 25
elif 500 <= salario <= 1000:
    aumento = salario / 100 * 20
elif 1000 <= salario <= 1500:
    aumento = salario / 100 * 15
elif 1500 <= salario <= 2000:
    aumento = salario / 100 * 10

# Imprimindo o novo salario mais o bonus
print(f"Seu aumento de R${aumento:.2f}, com seu bonus de R${bonus:.2f} é de:"
      f" \nR${((aumento + salario) + bonus):.2f}")
