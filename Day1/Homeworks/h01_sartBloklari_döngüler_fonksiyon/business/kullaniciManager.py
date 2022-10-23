from entities.kullanici import Kullanici
from fakeData.data import fData

class KullaniciManager:
    def __init__(self):
        self._user = fData()

    @property
    def uAdi(self):
        return self._user.uAdi

    @property
    def uSifre(self):
        return self._user.uSifre

    def bilgiDogrumu(self, user: Kullanici):
        if user.isim == self.uAdi and user.sifre == self.uSifre:
            return True
        return False
