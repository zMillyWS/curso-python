"""
1. Crie um programa que:
a) Crie/abra um arquivo texto de nome "arq.txt";
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere "0";
c) Feche o arquivo;
d) Abra, leia o arquivo e escreva na tela todos os conteúdos armazenados.
"""


def main():
    with open("arq.txt", "w") as file:
        while True:
            char = input("Digite um caractere (ou '0' para sair): ")
            if char == "0":
                break
            file.write(char + "\n")

    with open("arq.txt", "r") as file:
        contents = file.read()
        print("Conteúdo do arquivo:")
        print(contents)


if __name__ == "__main__":
    main()
