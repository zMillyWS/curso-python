"""
Exercicio 35 Secao - 05

35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""
dia, mes, ano = input("Digite uma data no formato dd/mm/aaaa:\n").split("/")
if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
    data = True
else:
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if ano > 0:  # Verifica se o ano é menor que zero.
        if 1 <= mes <= 12:  # Verifica se o mes esta entre 1 e 12.
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 \
                    or mes == 10 or mes == 12:  # Verifica se esta entre os meses que tem 31 dias
                if 1 <= dia <= 31:  # Verifica se o mes tem entre 1 e 31 dias
                    data = True
                else:
                    data = False
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:  # Veriica se esta entre os meses que tem 30 dias
                if 1 <= dia <= 30:  # Verifica se o mes tem entre 1 e 30 dias
                    data = True
                else:
                    data = False
            elif mes == 2:  # Verifica se é o mes 2.
                if ano % 4 == 0:  # Verifica se o ano é bissexto
                    if ano % 100 == 0:
                        if ano % 400 == 0:
                            if 1 <= dia <= 29:  # Se o ano for bissexto, fevereiro tem 29 dias.
                                data = True
                            else:
                                data = False
                        else:
                            if 1 <= dia <= 28:  # Se o ano não for bissexto, fevereiro tem 28 dias.
                                data = True
                            else:
                                data = False
                    else:
                        if 1 <= dia <= 29:
                            data = True
                        else:
                            data = False

                else:
                    if 1 <= dia <= 28:
                        data = True
                    else:
                        data = False

            else:
                data = False
        else:
            data = False
    else:
        data = False
if data:  # Verifica se a data é True
    print(f"A data {dia}/{mes}/{ano} é válida.")
else:
    print(f"A data {dia}/{mes}/{ano} é inválida.")
