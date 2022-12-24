from src import OgrenciDbKayıt
from src.Ogrenci import Ogrenci

import datetime



class OgrenciKayıt(object):

    def __init__(self):
        self.ogrenci = Ogrenci("", "", "", "", "", "", "", "", "","","","","","")


    def kayıt(self):
        print("Öğrencinin..\n")
        ad = input(" Adı : ")
        soyad = input(" Soyad : ")
        tc = input(" Tc kimlik : ")
        yas = input(" Yaşı : ")
        dogum_tarihi = input(" Doğum tarihi : ")
        okul = input(" Okulu : ")
        bolum = input(" Okuduğu Bölüm : ")
        ogrenci_tel = input(" Telefon Numarası : ")
        mail = input(" e posta adresi giriniz: ")
        veli_ad = input(" Veli Adı: ")
        veli_soyad = input(" Veli Soyad: ")
        veli_telefon = input(" Veli Telefon: ")
        veli_address = input(" Veli Address: ")
        kayit_tarihi = str(datetime.date.today())





        self.ogrenci = Ogrenci(ad.capitalize(),
                               soyad.capitalize(),
                               tc.capitalize(),
                               yas.capitalize(),
                               dogum_tarihi.capitalize(),
                               okul.capitalize(),
                               bolum.capitalize(),
                               ogrenci_tel.capitalize(),
                               mail.capitalize(),
                               kayit_tarihi,
                               veli_ad.capitalize(),
                               veli_soyad.capitalize(),
                               veli_telefon.capitalize(),
                               veli_address.capitalize())

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


