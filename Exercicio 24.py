"""
Exercicio 24 Secao - 05

24. Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
Faca um programa em que o usuário entre com o valor e o estado destino do produto e o programa
retorne o preco final do produto acrescido do imposto do estado em que ele será vendido.
Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""
def meu_switch(estado):
    opcoes = {
        "MG": f"O valor final do produto é R${(valor // 100 * 7) + valor:.2f}",
        "SP": f"O valor final do produto é R${(valor // 100 * 12) + valor:.2f}",
        "RJ": f"O valor final do produto é R${(valor // 100 * 15) + valor:.2f}",
        "MS": f"O valor final do produto é R${(valor // 100 * 8) + valor:.2f}",
    }
    return opcoes.get(estado, "Estado inválido, tente digitar apenas as siglas.")
valor = input("Digite o valor do produto: \nR$")
while valor.isalpha():
    print("Valor inserido ivalido. Por favor, insira apenas caracteres numéricos.")
    valor = input("Digite o valor do produto: \nR$")
valor = float(valor)
estado = input("Digite o estado de destino (em siglas):\n")
estado = estado.upper()
print(meu_switch(estado))
