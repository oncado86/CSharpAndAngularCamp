class Kurs:
    def __init__(self, kurs_adi, kurs_aciklamasi):
        self._kurs_adi = kurs_adi
        self._kurs_aciklamasi = kurs_aciklamasi

    @property
    def kurs_adi(self):
        return self._kurs_adi

    @kurs_adi.setter
    def kurs_adi(self, kurs_adi):
        self.kurs_adi = kurs_adi

    @property
    def kurs_aciklamasi(self):
        return self._kurs_aciklamasi

    @kurs_aciklamasi.setter
    def kurs_aciklamasi(self, kurs_aciklamasi):
        self.kurs_aciklamasi = kurs_aciklamasi
