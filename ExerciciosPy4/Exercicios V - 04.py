"""
Exercicios V - Secao 04
"""

# 41.
valor, horas = input('Digite o valor da hora de trabalhado e o numero de horas trabalhadas no mês: ').split()
salario = int(valor) * int(horas)
total = salario + (salario / 100 * 10)
print(f'O valor do mês a ser pago ao funcionario é de R${total:.2f}')

# 42.
salariob = input('Digite o salário base do funcionario: ')
salarioi = int(salariob) - (int(salariob) / 100 * 2)
print(f'O salario total desse funcionario é R${salarioi:.2f}')

# 43.
produto = input('Digite o valor do produto: ')
descontado = int(produto) - (int(produto) / 100 * 10)
parcela = int(produto) / 3
comissaoa = descontado / 100 * 5
comissaop = int(produto) / 100 * 5
print(f'O total a pagar a vista com desconto é R${descontado:.2f} '
      f'\nO valor parcelado em 3x sem juros é R${parcela:.2f}) '
      f'\nA comissao do vendedor, caso seja venda a vista é R${comissaoa:.2f}'
      f'\nA comissao do vendedor, no caso seja parcelada é R${comissaop:.2f}')

# 44.
a, b = input('Qual a altura do degrau e a altura que deseja alcancar? ').split()
obj = int(b) / int(a)
print(f'Para atingir a altura desejada voce deverá subir {int(obj)} degraus.')

# 45.
maiuscula = input("Digite uma palavra em caixa alta: ")
minuscula = maiuscula.lower()
print(f"{minuscula}")

# 46.
numcerto = input("Digite um número de 100 a 999: ")
print(numcerto[ : : - 1])

# 47.
numlido = input("Digite um número de 1000 a 9999: ")
print(numlido[0])
print(numlido[1])
print(numlido[2])
print(numlido[3])

# 48.
segt = int(input("Digite um valor em segundos: "))
hora = segt / 3600
hsobra = segt % 3600
minutos = hsobra / 60
segundos = segt % 60

print(f"Esse valor em Horas, minutos e segundos é: {hora:.0f}:{minutos:.0f}:{segundos:.0f}")

# 49.

ihora, imin, iseg = input("Digite o horário de início da experiencia em Horas, minutos e segundos: ").split()
d = int(input("Digite o tempo de duracao da experiencia, em segundos: "))
s_final = (int(iseg) + d) % 60
m_final = (int(imin) + (int(iseg) + d) / 60) % 60
h_final = (int(ihora) + (int(imin) + (int(iseg) + d) / 60) / 60 ) % 24
print(f"A experiencia terminou em: {h_final:.0f}:{m_final:.0f}:{s_final:.0f}")

# 50.
idade = int(input("Digite a idade que voce fará/fez este ano:"))
nasc = 2022 - idade
print(f"Voce nasceu em {nasc}")

# 51.
amg1, amg2, amg3 = input("Digite o nome dos três amigos: ").split()

invest1 = float(input(f"Digite o valor que o {amg1.title()} investiu: R$"))
invest2 = float(input(f"Digite o valor que o {amg2.title()} investiu: R$"))
invest3 = float(input(f"Digite o valor que o {amg3.title()} investiu: R$"))

premio = float(input("Digite o valor do premio: R$"))

soma = premio / (invest1 + invest2 + invest3)
premio_1 = soma * invest1
premio_2 = soma * invest2
premio_3 = soma * invest3

print(f"Para o valor do premio ser dividido igualmente de acordo com o investimento de cada um,\n"
      f" {amg1.title()} deverá receber R${premio_1:.2f}, {amg2.title()} deverá receber R${premio_2:.2f}"
      f"e {amg3.title()} deverá receber R${premio_3:.2f}")

# 52.
c, l = input("Digite as dimencoes do terreno, comprimento e largura: ").split()
valor = float(input("Digite o valor do metro da tela que deseja usar para cercar o terreno: "))

custo = (int(c) + int(c) + int(l) + int(l)) * valor

print(f"O custo para cercar este terreno com tela será de R${custo:.2f}")


