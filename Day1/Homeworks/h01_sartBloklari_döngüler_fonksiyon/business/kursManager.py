from entities.kurs import Kurs


class KursManager:
    def __init__(self):
        self._kurslar=[]
    
    @property
    def kurslar(self):
        return self._kurslar
    
    @kurslar.setter
    def kurslar(self, kurs:Kurs):
        self._kurslar.append(kurs)
    
    def kurslariListele(self):
        for k in self._kurslar:
            print(k.kurs_adi, k.kurs_aciklamasi)