"""
1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.

2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.

3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
"""


# 1
class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor: str):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor: str):
        self._modelo = valor

    def imprimir_dados(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


# 2
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int):
        super().__init__(marca, modelo)
        self._portas = portas

    @property
    def portas(self):
        return self._portas

    @portas.setter
    def portas(self, valor: int):
        if valor >= 0:
            self._portas = valor
        else:
            raise ValueError("O número de portas não pode ser negativo.")

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"Portas: {self.portas}")


# 3
if __name__ == "__main__":
    carro = Carro(marca="Toyota", modelo="Corolla", portas=4)
    carro.imprimir_dados()

    # Testando as propriedades
    carro.marca = "Honda"
    carro.modelo = "Civic"
    carro.portas = 2
    carro.imprimir_dados()

    # Testando o setter com valor inválido
    try:
        carro.portas = -1
    except ValueError as e:
        print(e)  # Exibe a mensagem de erro
    carro.imprimir_dados()  # Verifica se os dados permanecem inalterados
    carro.portas = 4  # Corrige o número de portas
    carro.imprimir_dados()  # Verifica se os dados foram atualizados corretamente
    carro.marca = "Ford"  # Atualiza a marca
    carro.modelo = "Focus"  # Atualiza o modelo
    carro.imprimir_dados()  # Verifica se os dados foram atualizados corretamente
