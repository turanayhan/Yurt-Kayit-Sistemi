from src.OgrenciKayıt import OgrenciKayıt


def ogrenci_ekle():
    print("Öğrenci Kayıt Ekranı..\n")
    turan = OgrenciKayıt()
    turan.kayıt()
    print("Öğrenci başarılı bir şekilde kaydedildi\n")

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
        print("1-Yeni Öğrenci Kayıt")
        print("2-Öğrenci kaydı sil")
        print("3-Öğrenci Ara")
        print("4-Tüm Öğrencileri Listele")
        print("5-Öğrenci Güncelle")

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