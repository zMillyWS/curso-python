"""
Exercicio 29 Secao - 05

29. Faca uma prova de matemática para criancas que estão aprendendo a somar números inteiros menores do que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
Qual é a soma de a + b? (Onde a e b são números aleatórios). Peca a resposta.
Faca cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas,
além de quantas vezes o aluno acertou.

"""
from random import randint
count = 0
acertos = 0
while count < 5:
    count = count + 1
    a = randint(0, 99)
    b = randint(0, 99)
    aResp = input(f"Questão {count}:\n {a} + {b} = ")
    resp = a + b
    while not aResp.isdigit():
        print("Por favor, digite a resposta em caracteres numérios. \n(Ex: 1, 2, 3...)")
        aResp = input(f"Questão {count}:\n {a} + {b} = ")
    aResp = int(aResp)
    if aResp != resp:
        print(f"Você errou. A soma de {a} + {b} é igual a {resp}.")
    else:
        print(f"Você acertou! A soma de {a} + {b} é igual a {resp}.")
        acertos = acertos + 1
print(f"Você acertou {acertos} de 5 questões.")
