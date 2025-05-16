"""
2. Faça um programa que tenha uma função que recebe uma data no formato string
exemplo "01/01/2024" e imprimaa ela por extenso como "1 de janeiro de 2024".
"""


def imprimir_data(data: str) -> str:
    """
    Imprime a data no formato 'dd/mm/aaaa'.

    :param data: Data no formato 'dd-mm-aaaa'.
    :return: Data formatada.
    """
    data_lista = data.split('/')
    dia = data_lista[0]
    mes = data_lista[1]
    ano = data_lista[2]
    match mes:
        case '01':
            mes = 'Janeiro'
        case '02':
            mes = 'Fevereiro'
        case '03':
            mes = 'Março'
        case '04':
            mes = 'Abril'
        case '05':
            mes = 'Maio'
        case '06':
            mes = 'Junho'
        case '07':
            mes = 'Julho'
        case '08':
            mes = 'Agosto'
        case '09':
            mes = 'Setembro'
        case '10':
            mes = 'Outubro'
        case '11':
            mes = 'Novembro'
        case '12':
            mes = 'Dezembro'
    return f"{dia} de {mes} de {ano}"


# Testando a função
data = input("Digite uma data no formato dd/mm/aaaa: ")
resultado = imprimir_data(data)
print(f"A data formatada é: {resultado}.")
