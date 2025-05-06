"""
Exercicio 08 Secao - 05

8. Faca um programa que leia 2 notas de um aluno, verifiquese as notas
sao válidas e exiba na tela a média destas notas.
"""
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
if nota1 < 0.0 or nota2 < 0.0:
    print("Nota esta errada")
elif nota1 > 10.0 or nota2 > 10.0:
    print("Nota não possui valor válido")
else:
    media = (nota1 + nota2) // 2
    print(f"A sua média é de: {media:.1f}")
