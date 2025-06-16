"""
faça um programa que receba o nome de um arquivo texto e mostre na tela quantas letras são vogais e quantas letras são consoantes.
"""
# Pode digitar example-text.txt como nome do arquivo por exemplo.


def contar_vogais_consoantes(nome_arquivo):
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    contador_vogais = 0
    contador_consoantes = 0

    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = (arquivo.read()).lower()
            for char in conteudo:
                if char in vogais:
                    contador_vogais += 1
                elif char in consoantes:
                    contador_consoantes += 1

        print(f"Vogais: {contador_vogais}, Consoantes: {contador_consoantes}")

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")


def main():
    nome_arquivo = input("Digite o nome do arquivo texto: ")
    contar_vogais_consoantes(nome_arquivo)


if __name__ == "__main__":
    main()
