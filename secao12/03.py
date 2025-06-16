"""
Faça um programa que receba do usuário o nome de um arquivo de texto e mostre na tela quantas linhas esse arquivo possui.
"""


def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            numero_linhas = len(linhas)
            print(f"O arquivo '{nome_arquivo}' possui {numero_linhas} linhas.")
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")


def main():
    nome_arquivo = input("Digite o nome do arquivo de texto: ")
    contar_linhas(nome_arquivo)


if __name__ == "__main__":
    main()
