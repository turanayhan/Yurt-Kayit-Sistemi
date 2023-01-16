import xml.etree.ElementTree as xml

from src.DeleteData import DeleteData
from src.GetData import GetData
from src.WindowPersonal import WindowPersonal
from src.WindowStudent import WindowStudent


class Admin(object):

    def __init__(self):
        self.admin()

    def ogrenci_ekle(self):

        print("Öğrenci Kayıt Ekranı..\n")
        studentpencere = WindowStudent()
        studentpencere.pencere_ac()
        self.student_menu()

    def ogrenciSil(self):
        tc = input("Silmek  istediğiniz öğrencinin tc kimlik numarasını giriniz : \n")
        DeleteData().delete_student(tc)
        print("Öğrenci kaydı silindi..")

        input("Çıkamk için herhangi bir tuşa basınız : \n")

    def ogrenciAra(self):
        tc = input("Ulaşmak istediğiniz öğrencinin tc kimlik numarasını giriniz : \n")
        student = GetData().student_bul(tc)
        print("Öğrenci bilgiler..")
        print(f'Öğrenci adı : {student.getAd()}')
        print(f'Öğrenci tc : {student.getTc()}')
        print(f'Öğrenci yas : {student.getYas()}')
        print(f'Öğrenci doğum tarihi : {student.getDt()}')
        print(f'Öğrenci gsm : {student.getGsm()}')
        print(f'Öğrenci mail : {student.getMail()}')
        print(f'Öğrenci okul : {student.getOkul()}')
        print(f'Öğrenci bölüm : {student.getBolum()}')
        print(f'Veli ad : {student.getVeli_ad()}')
        print(f'Veli gsm : {student.getVeli_gsm()}')
        print(f'Veli adres : {student.getVeli_address()}')
        print(f'Kayıt tarihi : {student.getKayıt_tarihi()}')

        input("Çıkamk için herhangi bir tuşa basınız : \n")

    def personal_sil(self):
        tc = input("Silmek istediğiniz öğrencinin tc kimlik numarasını giriniz : \n")
        DeleteData().delete_personal(tc)
        print("Personel kaydı silindi..")
        input("Çıkamk için herhangi bir tuşa basınız : \n")

    def personalekle(self):
        print("Personal Kayıt Ekranı..\n")
        personal_pencere = WindowPersonal()
        personal_pencere.pencere_ac()
        self.student_menu()

    def personal_ara(self):
        secim = input("Ulaşmak istediğiniz personelin tc kimlik numarasını giriniz : \n")
        personal = GetData().personal_bul(secim)
        print("Personel bilgiler..")
        print(f'Personel adı : {personal.getAd()}')
        print(f'Personel tc : {personal.getTc()}')
        print(f'personel yas : {personal.getYas()}')
        print(f'personel doğum tarihi : {personal.getDt()}')
        print(f'personel mail : {personal.getMail()}')
        print(f'personel unvanı : {personal.getUnvan()}')
        print(f'personel görevi : {personal.getGorevi()}')

        input("Çıkamk için herhanfi bir tuşa basınız : \n")

    def student_menu(self):
        while True:
            menu_veri = xml.parse("data/menu_student.xml")
            kok = menu_veri.getroot()
            for altseviye in kok:
                print(altseviye.text)
            secim = input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (0-7):\n")

            if secim == "1":
                self.ogrenci_ekle()
                break
            elif secim == "2":
                self.ogrenciSil()
            elif secim == "3":
                self.ogrenciAra()
            elif secim == "4":
                pass
            elif secim == "5":
                self.admin()
            else:
                print("\nMenu elemanlarından birini seçiniz...\n")
                continue

    def personal_menu(self):
        while True:
            menu_veri = xml.parse("data/menu_personal.xml")
            kok = menu_veri.getroot()

            for altseviye in kok:
                print(altseviye.text)
            secim = input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (0-7):\n")
            if secim == "1":
                self.personalekle()
                break
            elif secim == "2":
                self.personal_ara()

            elif secim == "3":
                self.personal_sil()

            elif secim == "4":
                self.admin()
            else:
                print("\nMenu elemanlarından birini seçiniz...\n")
                continue

    def admin(self):
        while True:
            print("Admin Giriş\n")
            tc = input("Tc kimlik numarası:\n")
            parola = input("Giriş şifresi :\n")

            if tc == "123456789" and parola == "1234":

                while True:
                    print("Giriş başarılı\n")
                    print("Öğrenci Birimi için 1 tuşlayın..")
                    print("Personel Birimi için 2 tuşlayın..")
                    birim = input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (1-2):\n")

                    if birim == "1":
                        self.student_menu()
                        break
                    elif birim == "2":
                        self.personal_menu()
                        break

            else:
                print("bilgilerinizi kontrol ediniz..")

