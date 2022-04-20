"""
Exercicio 37 Secao - 05

37. As tarifas de certo parque de estacionamento são as seguintes:
    - Primeira e Segunda hora = R$1,00 cada
    - Terceira e Quarta hora = R$1,40 cada
    - Quinta hora e seguintes = R$2,00 cada
O número de horas a pagar é sempre arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas.
Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida,
escreva na tela o preco cobrado pelo estacionamento.
"""
# Recebendo os horários
hora_che, min_che = input("Digite a hora de chegada (hh:mm):\n").split(":")
hora_part, min_part = input("Digite a hora de partida (hh:mm):\n").split(":")

# Verificando
while not hora_che.isdigit() or not hora_part.isdigit() or not min_che.isdigit() or not min_part.isdigit():
    print("Por favor, digite um horário válido, no formato HH:MM.")
    hora_che, min_che = input("Digite a hora de chegada (hh:mm):\n").split(":")
    hora_part, min_part = input("Digite a hora de partida (hh:mm):\n").split(":")

# Transformando em inteiros
hora_che = int(hora_che)
min_che = int(min_che)
hora_part = int(hora_part)
min_part = int(min_part)


# Transformando em minutos
t_che = (hora_che * 60) + min_che
t_part = (hora_part * 60) + min_part

# Reformulando caso tenha se passado mais de um dia
if t_che > t_part:
    t_part = (t_part + 1440)

# Contando o periodo de horas em que o carro ficou no estacionamento
if (t_part - t_che) % 60 > 0:
    periodo = ((t_part - t_che) // 60) + 1
else:
    periodo = (t_part - t_che) // 60

# Contando os valores de acordo com o período
if periodo <= 2:
    valor = periodo
elif 2 > periodo <= 4:
    valor = periodo * 1.40
else:
    valor = periodo * 2

print(f"O valor cobrado é de R${valor:.2f}, referente á {periodo} horas de estacionamento.")
