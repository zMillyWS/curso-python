"""
3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de
forma que:
a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
permitir que seja informado um número de canal para efetuar a troca;
"""


class Televisao:
    def __init__(self):
        self._status = False  # False = desligada, True = ligada
        self._volume = 10  # Volume inicial
        self._canal = 1  # Canal inicial

    @property
    def status(self):
        return self._status

    @property
    def volume(self):
        return self._volume

    @property
    def canal(self):
        return self._canal

    def ligar(self):
        self._status = True

    def desligar(self):
        self._status = False

    def aumentar_volume(self):
        if self._status:
            self._volume += 1

    def diminuir_volume(self):
        if self._status and self._volume > 0:
            self._volume -= 1

    def aumentar_canal(self):
        if self._status:
            self._canal += 1

    def diminuir_canal(self):
        if self._status and self._canal > 1:
            self._canal -= 1

    def mudar_canal(self, canal: int):
        if self._status and canal > 0:
            self._canal = canal


class ControleRemoto:
    def __init__(self, televisao: Televisao):
        self._televisao = televisao

    def ligar(self):
        self._televisao.ligar()

    def desligar(self):
        self._televisao.desligar()

    def aumentar_volume(self):
        self._televisao.aumentar_volume()

    def diminuir_volume(self):
        self._televisao.diminuir_volume()

    def aumentar_canal(self):
        self._televisao.aumentar_canal()

    def diminuir_canal(self):
        self._televisao.diminuir_canal()

    def mudar_canal(self, canal: int):
        self._televisao.mudar_canal(canal)


# Exemplo de uso
if __name__ == "__main__":
    tv = Televisao()
    controle = ControleRemoto(tv)

    print("Usando o controle remoto para gerenciar a TV:")
    controle.ligar()
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")

    controle.aumentar_volume()
    controle.aumentar_canal()
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")

    controle.mudar_canal(5)
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")

    controle.desligar()
    print(f"TV ligada: {tv.status}")
    controle.diminuir_volume()  # Não deve ter efeito, pois a TV está deslig
    controle.diminuir_canal()  # Não deve ter efeito, pois a TV está desligada
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")

    print("\nUsando a tv para gerenciar a TV:")
    tv.ligar()
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")
    tv.aumentar_volume()
    tv.aumentar_canal()
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")
    tv.mudar_canal(10)
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")
    tv.desligar()
    print(f"TV ligada: {tv.status}")
    tv.diminuir_volume()  # Não deve ter efeito, pois a TV está desligada
    tv.diminuir_canal()  # Não deve ter efeito, pois a TV está desligada
    print(f"TV ligada: {tv.status}, Volume: {tv.volume}, Canal: {tv.canal}")
