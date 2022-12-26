from src import OgrenciDbKayıt
from src.Ogrenci import Ogrenci



class OgrenciKayıt():

    def __init__(self):
        self.ogrenci = Ogrenci("", "", "", "", "", "", "", "", "","","","")



    def kayıt(self,ad,tc,yas,dogum_tarihi,okul,bolum,ogrenci_tel,mail,veli_ad,veli_telefon,veli_address,kayit_tarihi):



        self.ogrenci = Ogrenci(ad.capitalize(),
                               tc.capitalize(),
                               yas.capitalize(),
                               str(dogum_tarihi.capitalize()),
                               okul.capitalize(),
                               bolum.capitalize(),
                               ogrenci_tel.capitalize(),
                               mail.capitalize(),
                               kayit_tarihi,
                               veli_ad.capitalize(),
                               veli_telefon.capitalize(),
                               veli_address.capitalize(),)

        self.set_data(self.ogrenci)



    def getStudent(self):
        pass

    def set_data(self, ogrenci):

        ogrenci_veri= OgrenciDbKayıt
        ogrenci_veri.data_kaydet(
                               ogrenci.tam_isim(),
                               ogrenci.yas,
                               ogrenci.tc,
                               ogrenci.dogum_tarihi,
                               ogrenci.okul,
                               ogrenci.bolum,
                               ogrenci.gsm,
                               ogrenci.mail,
                               ogrenci.veli_ad,
                               ogrenci.veli_gsm,
                               ogrenci.veli_address,
                               ogrenci.kayit_tarihi)


