"""
Exercicio 14 Secao - 05

14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 á 10, respectivamente, a um trabalho de laboratório, a uma avaliacão semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos:
Trabalho de laboratório: 2;
Avaliacão Semestral: 3;
Exame FInal: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9),
de recuperacão (entre 3 e 4,9) ou se foi aprovado.
"""
nota1 = float(input("Digite a nota do Trabalho de Laboratório: "))
nota2 = float(input("Digite a nota da Avaliacao Semestral: "))
nota3 = float(input("Digite a nota do Exame Final: "))
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) // 10
if media <= 2.9:
    print(f"Sua media foi de {media:.1f}, você foi reprovado.")
elif media >= 5:
    print(f"Sua média foi de {media:.1f}, você foi aprovado")
else:
    print(f"Sua media foi de {media:.1f}, você ficou de recuperacao")
