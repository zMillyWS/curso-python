"""
Exercicio 34 Secao - 05

34. Leia a nota e o número da faltas de um aluno, e escreva seu conceito.
De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma reducão de conceito.
"""
nota = input("Digite a nota do aluno:\n")
faltas = input("Digite o número de faltas do aluno:\n")
while nota.isalpha() or not faltas.isdigit():
    print("Por favor digite apenas caracteres numéricos.")
    nota = input("Digite a nota do aluno:\n")
    faltas = input("Digite o número de faltas do aluno:\n")
nota = float(nota)
faltas = int(faltas)
if faltas <= 20:
    if nota >= 9:
        conceito = "A"
    elif 7.5 <= nota <= 8.9:
        conceito = "B"
    elif 5.0 <= nota <= 7.4:
        conceito = "C"
    elif 4.0 <= nota <= 4.9:
        conceito = "D"
    elif nota <= 3.9:
        conceito = "E"
else:
    if nota >= 9:
        conceito = "B"
    elif 7.5 <= nota <= 8.9:
        conceito = "C"
    elif 5.0 <= nota <= 7.4:
        conceito = "D"
    elif 4.0 <= nota <= 4.9:
        conceito = "E"
    elif nota <= 3.9:
        conceito = "E"
print(f"O concetio desse aluno é: {conceito}")
