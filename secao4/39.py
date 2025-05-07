"""
Exercício 39: Divida um prêmio de R$780.000 entre
três ganhadores com percentuais diferentes.
"""
total = 780_000
ganhador1 = total / 100 * 46
ganhador2 = total / 100 * 32
ganhador3 = total - (ganhador1 + ganhador2)
print(
    f"O primeiro ganhador recebeu R${ganhador1:.2f},"
    f"o segundo ganhador recebeu R${ganhador2:.2f} "
    f"e o terceiro ganhador recebeu R${ganhador3:.2f}"
)
