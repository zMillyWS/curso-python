"""
Exercicios IV - Secao 04
"""
# 31.
numero = int(input('Digite um número:'))
print(f'O antecessor de {numero} é {numero - 1} e o sucessor é {numero + 1}')

# 32.
numero2 = int(input('Digite um número:'))
print(f'O sucessor do triplo de {numero2} mais o antecessor do dobro de {numero2} é igual à '
      f'{(numero2 * 3 + 1) + (numero2 * 2 - 1)}')

# 33.
L = 5
print(f'Se o lado de um quadrado for igual à {L}, então sua área será igual à {L ** 2}')

# 34.
R = int(input('Diga o valor do raio do circulo '))
print(f'A área do círculo é {3.131592 * R ** 2}')

# 35.
a, b = input('Digite dois valores: ').split()
conta = int(a) ** 2 + int(b) ** 2
print(f'Se os catetos de um triangulo forem {a} e {b}, a hipotenusa é {conta}')

# 36.
altura, raio = input('Digite o valor da altura e do raio de um cilindro circular ').split()
v = 3.141592 * int(raio) ** 2 * int(altura)
print(f'O volume desse cilindro é {v:.2f}')

# 37.
valor = int(input('Digite o valor do produto:'))
desconto = valor / 100 * 12
print(f'Com desconto de 12% esse produto de R${valor:.2f} fica apenas R${valor - desconto:.2f}')

# 38.
salario = int(input('Digite o valor do seu salario:'))
aumento = salario / 100 * 25
print(f'Você recebeu um aumento de 25% e seu salario foi de R${salario:.2f} para R${salario + aumento:.2f}')

# 39.
total = 780_000
ganhador1 = total / 100 * 46
ganhador2 = total / 100 * 32
ganhador3 = total - (ganhador1 + ganhador2)
print(f'O primeiro ganhador recebeu R${ganhador1:.2f}, o segundo ganhador recebeu R${ganhador2:.2f} '
      f'e o terceiro ganhador recebeu R${ganhador3:.2f}')

# 40.
dias = int(input('Digite o número de dias que o encanador vai trabalhar: '))
salariob = dias * 30
salariol = salariob - (salariob / 100 * 8)
print(f'O salario liquido do encanador é R${salariol:.2f}')
