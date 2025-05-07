"""
Exercício 48: Converta um valor em segundos para horas, minutos e segundos.
"""
segt = int(input("Digite um valor em segundos: "))
hora = segt / 3600
hsobra = segt % 3600
minutos = hsobra / 60
segundos = segt % 60

print(
    f"Esse valor em Horas, minutos e segundos é: {hora:.0f}:{minutos:.0f}:{
        segundos:.0f}"
)
