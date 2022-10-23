from fakeData.data import fData
from business.kullaniciManager import KullaniciManager
from business.kursManager import KursManager
from entities.kurs import Kurs
from entities.kullanici import Kullanici


class RecapDemo:
    def __init__(self):
        self._user = fData()

    @property
    def uAdi(self):
        return self._user.uAdi

    @property
    def uSifre(self):
        return self._user.uSifre

    def bilgiAl(self, mesaj):
        return input(f"{mesaj}: ")


rd = RecapDemo()
kurs_m = KursManager()
kullanici_m = KullaniciManager()
kullanici = Kullanici(rd.bilgiAl("Lütfen isminizi giriniz: "),
                      rd.bilgiAl("Lütfen sifrenizi giriniz: "))

kurs_m.kurslar = Kurs("C# + Angular", "Yazılım Geliştirici Yetiştirme Kampı")
kurs_m.kurslar = Kurs("Java + React", "Yazılım Geliştirici Yetiştirme Kampı")


if kullanici_m.bilgiDogrumu(kullanici):
    print(f"Hoş geldiniz: {kullanici.isim}")
    kurs_m.kurslariListele()
else:
    print("Bilgiler hatalı")
