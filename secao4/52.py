"""
Exercício 52: Calcule o custo para cercar um terreno com tela,
dado o comprimento, largura e valor do metro.
"""
comprimento, largura = input("Digite as dimensões do terreno,"
                             "comprimento e largura: ").split()
valor = float(
    input("Digite o valor do metro da tela que"
          "deseja usar para cercar o terreno: ")
)

custo = (int(comprimento) + int(comprimento) +
         int(largura) + int(largura)) * valor

print(f"O custo para cercar este terreno com tela será de R${custo:.2f}")
