"""
Exercicio 09 Secao - 05

9. Leia o salário de um trabalhador e o valor da prestacao de um emprestimo.
Se a prestacao for maior que 20% do salario imprima:"Emprestimo não concedido".
Caso contrário imprima: "Empréstimo concedido".
"""
salario = float(input("Digite o seu salário: R$"))
valor = float(input("Digite o valor da prestacao do empréstimo: R$"))
porcent = salario / 100 * 20
if valor > porcent:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")