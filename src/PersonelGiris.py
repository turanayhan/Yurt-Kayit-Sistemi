from src import Tks
from src.OgrenciKayıt import OgrenciKayıt
from src.Tks import Tk
import xml.etree.ElementTree as xml
from datetime import date



def ogrenci_ekle():


    print("Öğrenci Kayıt Ekranı..\n")

    Tks.pencere_ac()
    menu()





def ogrenciSil():
    pass


def ogrenciAra():
    pass


def ogrenciGuncelle():
    pass

def tumunuListele():
    pass



def menu():
    while True:


        menu_veri = xml.parse("data/menu.xml")
        kok = menu_veri.getroot()
        for altseviye in kok:
            print(altseviye.text)

        secim = input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (0-7):\n")

        if secim == "1":

            ogrenci_ekle()
            break

        elif secim == "2":

            ogrenciSil()

        elif secim == "3":

            ogrenciAra()

        elif secim == "4":

            tumunuListele()

        elif secim == "5":

            ogrenciGuncelle()


        else:
            print("\nMenu elemanlarından birini seçiniz...\n")
            continue


menu()