from entities.kullanici import Kullanici


class fData:
    def __init__(self):
        self._user = Kullanici("OnCaDo", "123")

    @property
    def uAdi(self):
        return self._user.isim

    @property
    def uSifre(self):
        return self._user.sifre
