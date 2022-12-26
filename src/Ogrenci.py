from src.Veli import Veli
from src.İnsan import İnsan


# İnsan ve veli sınıfından miras alıyor
class Ogrenci(İnsan, Veli):

    # Constructor
    def __init__(self, ad, tc, yas, dogum_tarihi, okul, bolum, gsm, mail,veli_ad,veli_gsm,veli_address, kayit_tarihi):
        İnsan.__init__(self, ad, tc, yas, dogum_tarihi)
        Veli.__init__(self, veli_ad, veli_gsm, veli_address)
        self.okul = okul
        self.gsm = gsm
        self.mail = mail
        self.bolum = bolum
        self.kayit_tarihi = kayit_tarihi

    def tam_isim(self):
        pass







