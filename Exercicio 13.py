"""
Exercicio 13 Secao - 05

13. Faca um algaritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda tem peso 1 e a terceira tem peso 2.
Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovacao deve ser igual ou supeior a 60 pontos.
"""
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
media = (nota1 + nota2 + nota3 * 2) // 4
if media >= 60:
    print(f"Sua média foi de {media:.1f}, você foi aprovado!")
else:
    print(f"Sua média foi de {media:.1f}, você foi reprovado.")
