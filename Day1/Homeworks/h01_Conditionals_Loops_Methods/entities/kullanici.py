class Kullanici:
    def __init__(self, name, password):
        self._name = name
        self._password = password

    @property
    def isim(self):
        return self._name

    @isim.setter
    def isim(self, isim):
        self._name = isim

    @property
    def sifre(self):
        return self._password
