"""
Exercicio 38 Secao - 05

38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês, Ano.
Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido.
Teste a validade do mês. Teste a validade do ano.
"""
# Recendo a data
dia, mes, ano = input("Digite a data de nascimento (dd/mm/aaaa):\n").split("/")

# Verificando validade do formato
while not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
    print("Por favor, forneca uma data válida, no formato DD/MM/AAAA.")
    dia, mes, ano = input("Digite a data de nascimento (dd/mm/aaaa):\n").split("/")

while not len(ano) == 4 or len(dia) > 2 or len(mes) > 2:
    print("Por favor, forneca uma data válida, no formato DD/MM/AAAA.")
    dia, mes, ano = input("Digite a data de nascimento (dd/mm/aaaa):\n").split("/")

# Verificando se ano é bissexto
bissexto = False
ano = int(ano)
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        bissexto = True
    else:
        bissexto = True
else:
    bissexto = False

# Verificando meses e dias
mes = int(mes)
dia = int(dia)
datavalida = False
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if 1 <= dia <= 31:
        datavalida = True
elif mes == 2:
    if bissexto:
        if 1 <= dia <= 29:
            datavalida = True
    else:
        if 1 <= dia <= 28:
            datavalida = True
else:
    if 1 <= dia <= 30:
        datavalida = True

# Verificando o ano
if ano > 2022:
    datavalida = False

# Vendo se a data é valida
if datavalida:
    print("Data válida.")
else:
    print("Data inválida.")
