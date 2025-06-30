"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.
"""


class Pessoa:
    def __init__(self, nome, data_nascimento, email):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self._data_nascimento = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    def imprimir_dados(self):
        print(f"Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, Email: {self.email}")


# Exemplo de uso
if __name__ == "__main__":
    pessoa = Pessoa("João Silva", "01/01/1990", "joao.silva@example.com")
    pessoa.imprimir_dados()
