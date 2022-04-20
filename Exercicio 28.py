"""
Exercicio 28 Secao - 05

28. Faca um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes
médias de acordo com um valor numérico digitado pelo usuário:
Geométrica;
Ponderada;
Harmônica;
Aritmética.
"""


def escolhas(media):
    opcoes = {
        "A": f"Você escolheu Geométrica, e o resultado é:{(x * y * z) ** (1/3):.2f}",
        "B": f"Você escolheu Ponderada, e o resultado é: {(x + 2 * y + 3 * z) // 6:.2f}",
        "C": f"Você escolheu Harmônica, e o resultado é: {1 // (1/x + 1/y + 1/z):.2f}",
        "D": f"Você escolheu Aritmética, e o resultado é: {(x + y + z) // 3:.2f}"
    }
    return opcoes.get(media, "Opcão inválida, tente novamente.")


x, y, z = input("Digite três números inteiros positivos:\n").split()
while not x.isdigit() or not y.isdigit() or not z.isdigit():
    print("Por favor, digite apenas números inteiros (sem vírgula).")
    x, y, z = input("Digite três números inteiros positivos: \n").split()
x = int(x)
y = int(y)
z = int(z)
media = input("Por favor escolha uma das seguintes médias:\n A) Geométrica\n "
              "B) Ponderada\n C) Harmônica\n D) Aritmética \nLetra: ")
media = media.upper()
print(escolhas(media))
