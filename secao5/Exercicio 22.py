"""
Exercicio 22 Secao - 05

22. Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou não se aposentar.
As condicoes para aposentaria são:
- Ter pelo menos 65 anos;
- Ou ter trabalhado pelo menos 30 anos;
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""
idade = input("Qual a idade do trabalhador? ")
tempo = input("Digite o tempo de servico deste trabalhador (em anos): ")
while idade.isalpha() or tempo.isalpha():
    print("Valor inválido. Por favor utilize apenas caracteres numéricos.")
    idade = input("Qual a idade do trabalhador? ")
    tempo = input("Digite o tempo de servico deste trabalhador: ")
if int(idade) >= 65 or int(tempo) >= 30:
    print("O trabalhador pode se aposentar.")
elif int(idade) >= 60 and int(tempo) >= 25:
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador ainda não pode se aposentar.")
