"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""


class Contato:
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"


class Agenda:
    def __init__(self):
        self._contatos = []

    def armazenar_contato(self, contato: Contato):
        self._contatos.append(contato)

    def remover_contato(self, contato: Contato):
        if contato in self._contatos:
            self._contatos.remove(contato)

    def buscar_contato(self, nome: str):
        for index, contato in enumerate(self._contatos):
            if contato.nome == nome:
                return index
        return -1

    def imprimir_agenda(self):
        for contato in self._contatos:
            print(contato)

    def imprimir_contato(self, indice: int):
        if 0 <= indice < len(self._contatos):
            print(self._contatos[indice])
        else:
            print("Índice inválido.")


# Exemplo de uso
if __name__ == "__main__":
    agenda = Agenda()

    contato1 = Contato("Alice", "1234-5678", "alice@example.com")
    contato3 = Contato("Carlos", "1023-5039", "carlos@example.com")
    contato2 = Contato("Bob", "9876-5432", "bob@example.com")

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)

    print("Agenda inicial:")
    agenda.imprimir_agenda()

    print("\nBuscando contato 'Carlos':")
    indice = agenda.buscar_contato("Carlos")
    print(f"Contato 'Carlos' encontrado no índice: {indice}")
    agenda.imprimir_contato(indice)

    agenda.remover_contato(contato1)
    print("\nAgenda após remover Alice:")
    agenda.imprimir_agenda()
