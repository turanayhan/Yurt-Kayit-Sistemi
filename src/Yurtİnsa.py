
import xml.etree.ElementTree as xml
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
import tkinter
from tkinter import *
from tkinter import messagebox




class Admin(object):

    def __init__(self):
        self.admin()
        pass




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
        print(personal_pencere.getTc())
        self.personal_menu()

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


class DbPush:
    def __init__(self):
        pass

    def student_kaydet(self, ad_, tc_, yas_, dg_tarihi_, okul_, bolum_, gsm_, mail_, veli_ad_, veli_gsm_, veli_address_,
                       kayit_tarihi_):



        studentData = ET.parse("data/database.xml")
        # En üst seviye XML etiketinin ne olduğunu bulalım
        kok = studentData.getroot()
        # Eleman eklemek
        for ogrenciler in kok.findall("Öğrenciler"):
            ogrenci = ET.SubElement(ogrenciler, f'id{tc_}')
            tc = ET.SubElement(ogrenci, 'Tc')
            ad = ET.SubElement(ogrenci, 'Ad')
            yas = ET.SubElement(ogrenci, 'Yas')
            dogum_tarihi = ET.SubElement(ogrenci, 'DogumTarihi')
            gsm = ET.SubElement(ogrenci, 'Gsm')
            mail = ET.SubElement(ogrenci, 'Mail')
            okul = ET.SubElement(ogrenci, 'Okul')
            bolum = ET.SubElement(ogrenci, 'Bolum')
            veli_ad = ET.SubElement(ogrenci, 'VeliAd')
            veli_gsm = ET.SubElement(ogrenci, 'VeliGsm')
            veli_address = ET.SubElement(ogrenci, 'VeliAddress')
            kayıt_tarihi = ET.SubElement(ogrenci, 'KayitTarihi')

            # değerleri atıyoruz

            tc.text = tc_
            ad.text = ad_
            yas.text = yas_
            tc.text = tc_
            mail.text = mail_
            gsm.text = gsm_
            okul.text = okul_
            bolum.text = bolum_
            veli_ad.text = veli_ad_
            veli_gsm.text = veli_gsm_
            veli_address.text = veli_address_
            dogum_tarihi.text = dg_tarihi_
            kayıt_tarihi.text = kayit_tarihi_
            studentData.write("data/database.xml", encoding="UTF-8")

    def Personal_kaydet(self, ad_, tc_, yas_, dg_tarihi_, unvan_, gorevi_, mail_):
        personalData = ET.parse("data/database.xml")
        # En üst seviye XML etiketinin ne olduğunu bulalım
        kok = personalData.getroot()

        for ogrenciler in kok.findall("Personeller"):
            ogrenci = ET.SubElement(ogrenciler, f'id{tc_}')
            tc = ET.SubElement(ogrenci, 'Tc')
            ad = ET.SubElement(ogrenci, 'Ad')
            yas = ET.SubElement(ogrenci, 'Yas')
            dg_tarihi = ET.SubElement(ogrenci, 'DogumTarihi')
            unvan = ET.SubElement(ogrenci, 'Unvan')
            gorevi = ET.SubElement(ogrenci, 'Gorevi')
            mail = ET.SubElement(ogrenci, 'Mail')

            tc.text = tc_
            ad.text = ad_
            yas.text = yas_
            dg_tarihi.text = dg_tarihi_
            mail.text = mail_
            unvan.text = unvan_
            gorevi.text = gorevi_
            personalData.write("data/database.xml", encoding="UTF-8")

class DeleteData:
  def __init__(self):
    self.tree = ElementTree()
    self.tree.parse('data/database.xml')


  def delete_personal(self,tc_kimlik):
    id = f'id{tc_kimlik}'
    personals = self.tree.findall('Personeller')
    for personal in personals:

      childs = personal.findall(id)
      for child in childs:

        personal.remove(child)

    self.tree.write("data/database.xml", encoding="UTF-8")


  def delete_student(self,tc_kimlik):
    id = f'id{tc_kimlik}'
    students = self.tree.findall('Öğrenciler')
    for personal in students:
      childs = personal.findall(id)
      for child in childs:
        personal.remove(child)

    self.tree.write("data/database.xml", encoding="UTF-8")
    QueePop().kuyruktan_sil()
    print("yedek listesinden asil kayıt yapıldı")



class GetData:

    def __init__(self):
        self.data = xml.parse("data/database.xml")

    def personal_bul(self, tc_no):
        kok = self.data.getroot().iter("Personeller")

        for child in kok:
            id = f'id{tc_no}'
            tc = child.find(id).find("Tc").text
            ad = child.find(id).find("Ad").text
            yas = child.find(id).find("Yas").text
            dogum_tarihi = child.find(id).find("DogumTarihi").text
            unvan = child.find(id).find("Unvan").text
            gorevi = child.find(id).find("Gorevi").text
            mail = child.find(id).find("Mail").text

            personal = Personal(ad, tc, yas, dogum_tarihi, unvan, gorevi, mail)

            return personal

    def student_bul(self, tc_no):
        kok = self.data.getroot().iter("Öğrenciler")

        for child in kok:
            id = f'id{tc_no}'
            tc = child.find(id).find("Tc").text
            ad = child.find(id).find("Ad").text
            yas = child.find(id).find("Yas").text
            dogum_tarihi = child.find(id).find("DogumTarihi").text
            gsm = child.find(id).find("Gsm").text
            okul = child.find(id).find("Okul").text
            mail = child.find(id).find("Mail").text
            bolum = child.find(id).find("Bolum").text
            veli_ad = child.find(id).find("VeliAd").text
            veli_gsm = child.find(id).find("VeliGsm").text
            veli_addrees = child.find(id).find("VeliAddress").text
            kayit_tarihi = child.find(id).find("KayitTarihi").text
            student = Student(ad, tc, yas, dogum_tarihi, okul, bolum, gsm, mail, veli_ad, veli_gsm, veli_addrees,
                              kayit_tarihi)
            return student


class Human(ABC):
    # Constructor
    def __init__(self, ad, tc, yas, dogum_tarihi):
        self.__ad = ad
        self.__tc = tc
        self.__dogum_tarihi = dogum_tarihi
        self.__yas = yas

    def getAd(self):
        return self.__ad

    def getTc(self):
        return self.__tc

    def getDt(self):
        return self.__dogum_tarihi

    def getYas(self):
        return self.__yas





class Quee:
    def __init__(self):
        pass

    def student_kaydet(self, ad_, tc_, yas_, dg_tarihi_, okul_, bolum_, gsm_, mail_, veli_ad_, veli_gsm_, veli_address_,
                    kayit_tarihi_):
        studentData = ET.parse("data/yedekler.xml")
        # En üst seviye XML etiketinin ne olduğunu bulalım
        kok = studentData.getroot()
        # Eleman eklemek
        for ogrenciler in kok.findall("Öğrenciler"):
            ogrenci = ET.SubElement(ogrenciler, f'id{tc_}')
            tc = ET.SubElement(ogrenci, 'Tc')
            ad = ET.SubElement(ogrenci, 'Ad')
            yas = ET.SubElement(ogrenci, 'Yas')
            dogum_tarihi = ET.SubElement(ogrenci, 'DogumTarihi')
            gsm = ET.SubElement(ogrenci, 'Gsm')
            mail = ET.SubElement(ogrenci, 'Mail')
            okul = ET.SubElement(ogrenci, 'Okul')
            bolum = ET.SubElement(ogrenci, 'Bolum')
            veli_ad = ET.SubElement(ogrenci, 'VeliAd')
            veli_gsm = ET.SubElement(ogrenci, 'VeliGsm')
            veli_address = ET.SubElement(ogrenci, 'VeliAddress')
            kayıt_tarihi = ET.SubElement(ogrenci, 'KayitTarihi')

            #değerleri atıyoruz

            tc.text = tc_
            ad.text = ad_
            yas.text = yas_
            tc.text = tc_
            mail.text = mail_
            gsm.text = gsm_
            okul.text = okul_
            bolum.text = bolum_
            veli_ad.text = veli_ad_
            veli_gsm.text = veli_gsm_
            veli_address.text = veli_address_
            dogum_tarihi.text = dg_tarihi_
            kayıt_tarihi.text = kayit_tarihi_
            studentData.write("data/yedekler.xml", encoding="UTF-8")


    def Personal_kaydet(self,ad_, tc_, yas_, dg_tarihi_, unvan_,gorevi_,mail_):
        personalData = ET.parse("data/yedekler.xml")
        # En üst seviye XML etiketinin ne olduğunu bulalım
        kok = personalData.getroot()

        for ogrenciler in kok.findall("Personeller"):
            ogrenci = ET.SubElement(ogrenciler, f'id{tc_}')
            tc = ET.SubElement(ogrenci, 'Tc')
            ad = ET.SubElement(ogrenci, 'Ad')
            yas = ET.SubElement(ogrenci, 'Yas')
            dg_tarihi = ET.SubElement(ogrenci, 'DogumTarihi')
            unvan = ET.SubElement(ogrenci, 'Unvan')
            gorevi = ET.SubElement(ogrenci, 'Gorevi')
            mail = ET.SubElement(ogrenci, 'Mail')

            tc.text = tc_
            ad.text = ad_
            yas.text = yas_
            dg_tarihi.text = dg_tarihi_
            mail.text = mail_
            unvan.text=unvan_
            gorevi.text=gorevi_
            personalData.write("data/yedekler.xml", encoding="UTF-8")


class QueePop:
    def __init__(self):
        self.tree = ElementTree()
        self.tree.parse('data/yedekler.xml')

    def kuyruktan_sil(self):
        Yedekler = self.tree.findall('Öğrenciler')

        for yedek in Yedekler:

            print(yedek[0].find('Tc').text)

            #kuyruktaki ilk elamanı database ekliyor

            DbPush().student_kaydet(yedek[0].find('Ad').text, yedek[0].find('Tc').text, yedek[0].find('Yas').text,
                                    yedek[0].find('DogumTarihi').text, yedek[0].find('Okul').text,
                                    yedek[0].find('Bolum').text, yedek[0].find('Gsm').text, yedek[0].find('Mail').text,
                                    yedek[0].find('VeliAd').text,
                                    yedek[0].find('VeliGsm').text, yedek[0].find('VeliAddress').text,
                                    yedek[0].find('KayitTarihi').text
                                    )

            for child in range(1):
                yedek.remove(yedek[child])

        self.tree.write("data/yedekler.xml", encoding="UTF-8")


class SaveData():
    def __init__(self):
        self.okuma=open("data/capacity.txt","r").read()


    def student_save(self, ad, tc, yas, dogum_tarihi, okul, bolum, ogrenci_tel, mail, veli_ad, veli_telefon,
                     veli_address,
                     kayit_tarihi):
        student = Student(ad.capitalize(),
                          tc.capitalize(),
                          yas.capitalize(),
                          str(dogum_tarihi.capitalize()),
                          okul.capitalize(),
                          bolum.capitalize(),
                          ogrenci_tel.capitalize(),
                          mail.capitalize(),
                          veli_ad.capitalize(),
                          veli_telefon.capitalize(),
                          veli_address.capitalize(),
                          kayit_tarihi)

        self.set_data1(student)

    def set_data1(self, student):
        # kapasite doluysa yedeklere alacak
        if self.okuma== "0":
            student_data = Quee()
            student_data.student_kaydet(
                student.getAd(),
                student.getTc(),
                student.getYas(),
                student.getDt(),
                student.getOkul(),
                student.getBolum(),
                student.getGsm(),
                student.getMail(),
                student.getVeli_ad(),
                student.getVeli_gsm(),
                student.getVeli_address(),
                student.getKayıt_tarihi())




        else:
            student_data = DbPush()
            student_data.student_kaydet(
                student.getAd(),
                student.getTc(),
                student.getYas(),
                student.getDt(),
                student.getOkul(),
                student.getBolum(),
                student.getGsm(),
                student.getMail(),
                student.getVeli_ad(),
                student.getVeli_gsm(),
                student.getVeli_address(),
                student.getKayıt_tarihi())
            capacity=int(self.okuma)-1
            okuma = open("data/capacity.txt", "w")
            okuma.write(str(capacity))



    def personalsave(self, ad, tc, yas, dogum_tarihi, unvan, gorevi, mail):
        personal = Personal(ad.capitalize(), tc.capitalize(), yas.capitalize(), dogum_tarihi.capitalize(),
                            unvan.capitalize(), gorevi.capitalize(), mail.capitalize())
        self.set_data2(personal)

    def set_data2(self, personal):
        student_data = DbPush()
        student_data.Personal_kaydet(personal.getAd(),
                                     personal.getTc(),
                                     personal.getYas(),
                                     personal.getDt(),
                                     personal.getUnvan(),
                                     personal.getGorevi(),
                                     personal.getMail()

                                     )

class Contact(ABC):
    def __init__(self,gsm,mail):
        self.__gsm=gsm
        self.__mail=mail


    @abstractmethod

    def getGsm(self):
        return self.__gsm

    def getMail(self):

        return self.__mail

class Student(Human,Contact):

    # Constructor
    def __init__(self, ad="", tc="", yas="", dogum_tarihi="", okul="", bolum="", gsm="", mail="", veli_ad="",
                 veli_gsm="", veli_address="", kayit_tarihi=""):
        Human.__init__(self, ad, tc, yas, dogum_tarihi)
        Contact.__init__(self, gsm, mail)
        self.__veli_ad = veli_ad
        self.__veli_gsm = veli_gsm
        self.__gsm2 = gsm
        self.__veli_address = veli_address
        self.__okul = okul
        self.__bolum = bolum
        self.__kayit_tarihi = kayit_tarihi

    def getVeli_ad(self):
        return self.__veli_ad

    def getVeli_gsm(self):
        return self.__veli_gsm

    def getVeli_address(self):
        return self.__veli_address

    def getOkul(self):
        return self.__okul

    def getGsm(self):
        return self.__gsm2

    def getBolum(self):
        return self.__bolum

    def getKayıt_tarihi(self):
        return self.__kayit_tarihi


class Personal(Human,Contact):
    def __init__(self, ad, tc, yas, dogum_tarihi, unvan, gorevi, mail):
        Human.__init__(self, ad, tc, yas, dogum_tarihi)
        Contact.__init__(self, "4222", mail)
        self.__unvan = unvan
        self.__gorevi = gorevi

    def getUnvan(self):
        return self.__unvan

    def getGorevi(self):
        return self.__gorevi

    def getGsm(self):
        return "422"

class WindowPersonal(tkinter.Tk):

    def __init__(self):

        self.tc_no = ""
        super().__init__()
        self.geometry("360x550")
        self.title("Personel Kayıt Ekanı")
        self.configure(bg='#D9ECF4')
        self.resizable(FALSE, FALSE)

        self.lb1 = Label(self, text="Ad Soyad :", width=15, font=("arial", 12), justify=tkinter.RIGHT, bg='#D9ECF4')
        self.lb1.place(x=15, y=50)
        self.ad = Entry(self)
        self.ad.place(x=200, y=50)

        self.lb2 = Label(self, text="Tc Kimlik no :", width=15, font=("arial", 12), justify=tkinter.RIGHT, bg='#D9ECF4')
        self.lb2.place(x=15, y=100)
        self.tc = Entry(self)
        self.tc.place(x=200, y=100)

        self.lb3 = Label(self, text="Personel Yaşı :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb3.place(x=15, y=150)
        self.yas = Entry(self)
        self.yas.place(x=200, y=150)



        self.lb5 = Label(self, text="İş Unvanı :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb5.place(x=15, y=200)
        self.unvan = Entry(self)
        self.unvan.place(x=200, y=200)

        self.lb6 = Label(self, text="Telefon Numarası :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb6.place(x=15, y=250)
        self.ogrenci_gsm = Entry(self)
        self.ogrenci_gsm.place(x=200, y=250)

        self.lb7 = Label(self, text="Doğum Tarihi :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb7.place(x=15, y=300)
        self.dogum_tarihi = Entry(self)
        self.dogum_tarihi.place(x=200, y=300)

        self.lb8 = Label(self, text="E Posta Adresi  :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb8.place(x=15, y=350)
        self.mail = Entry(self)
        self.mail.place(x=200, y=350)

        self.lb9 = Label(self, text="Görevi  :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb9.place(x=15, y=400)
        self.gorevi = Entry(self)
        self.gorevi.place(x=200, y=400)

        self.lb5 = Label(self, text="Bölümü :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb5.place(x=15, y=450)
        self.bolum = Entry(self)
        self.bolum.place(x=200, y=450)

        self.btKaydet = tkinter.Button(self, command=self.kaydet, text="Kaydet", width=15, font=("arial", 12),bg='#D9ECF4')
        self.btKaydet.place(x=100, y=500)




    def kaydet(self):
        self.tc_no=self.tc.get()
        personalKayıt = SaveData()
        bugun = str(datetime.datetime.today())
        if ((self.ad.get() == "") or (self.tc.get() == "") or (self.yas.get() == "") or (self.dogum_tarihi.get() == "") or (self.bolum.get() == "") or
                (self.ogrenci_gsm.get() == "") or (self.mail.get() == "") ):

            messagebox.showinfo("durum", "Boş alanları doldurunuz..")


        else:
            personalKayıt.personalsave(self.ad.get().capitalize(), self.tc.get().capitalize(), self.yas.get().capitalize(), self.dogum_tarihi.get(),
                        self.unvan.get().capitalize(), self.gorevi.get().capitalize(),self.mail.get().capitalize())
            print("Personel başarılı bir şekilde kaydedildi\n")
            messagebox.showinfo("durum", "Personel Başarılı bir şekilde kaydedildi..")

            self.destroy()








    def pencere_ac(self):
        self.mainloop()

    def getTc(self):
        return  self.tc_no

class WindowStudent(tkinter.Tk):

    def __init__(self):

        self.tc_no=""
        super().__init__()
        self.geometry("360x700")
        self.title("Öğrenci Kayıt Ekanı")
        self.configure(bg='#D9ECF4')
        self.resizable(FALSE, FALSE)

        self.lb1 = Label(self, text="Öğrenci Ad Soyad :", width=15, font=("arial", 12), justify=tkinter.RIGHT, bg='#D9ECF4')
        self.lb1.place(x=15, y=50)
        self.ad = Entry(self)
        self.ad.place(x=200, y=50)

        self.lb2 = Label(self, text="Tc Kimlik no :", width=15, font=("arial", 12), justify=tkinter.RIGHT, bg='#D9ECF4')
        self.lb2.place(x=15, y=100)
        self.tc = Entry(self)
        self.tc.place(x=200, y=100)

        self.lb3 = Label(self, text="Öğrenci Yaşı :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb3.place(x=15, y=150)
        self.yas = Entry(self)
        self.yas.place(x=200, y=150)

        self.list_of_cntry = (
        "İnöü üniversitesi", "Turgut Özal Üniversitesi", "Fırat Üniveristesi", "Eskişehir Üniveristesi")
        self.cv = StringVar()
        self.drplist = OptionMenu(self, self.cv, *self.list_of_cntry)
        self.drplist.config(width=14)
        self.cv.set("Seç")
        self.lb4 = Label(self, text="Kayıtlı üniversite :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb4.place(x=15, y=200)
        self.drplist.place(x=200, y=200)

        self.lb5 = Label(self, text="Okuduğu Bölüm :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb5.place(x=15, y=250)
        self.bolum = Entry(self)
        self.bolum.place(x=200, y=250)

        self.lb6 = Label(self, text="Telefon Numarası :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb6.place(x=15, y=300)
        self.ogrenci_gsm = Entry(self)
        self.ogrenci_gsm.place(x=200, y=300)

        self.lb7 = Label(self, text="Doğum Tarihi :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb7.place(x=15, y=350)
        self.dogum_tarihi = Entry(self)
        self.dogum_tarihi.place(x=200, y=350)

        self.lb8 = Label(self, text="E Posta Adresi  :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb8.place(x=15, y=400)
        self.mail = Entry(self)
        self.mail.place(x=200, y=400)

        self.lb9 = Label(self, text="Veli Ad Soyad  :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb9.place(x=15, y=450)
        self.veli_ad = Entry(self)
        self.veli_ad.place(x=200, y=450)

        self.lb10 = Label(self, text="Veli Telefon  :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb10.place(x=15, y=500)
        self.veli_gsm = Entry(self)
        self.veli_gsm.place(x=200, y=500)

        self.lb11 = Label(self, text="Veli Adress  :", width=15, font=("arial", 12), justify=tkinter.LEFT, bg='#D9ECF4')
        self.lb11.place(x=15, y=550)
        self.veli_address = Entry(self)
        self.veli_address.place(x=200, y=550)

        self.btKaydet = tkinter.Button(self, command=self.kaydet,text="Kaydet", width=15, font=("arial", 12), bg='#D9ECF4')
        self.btKaydet.place(x=100, y=650)








    def kaydet(self):

        self.tc_no=self.tc.get()
        og_kayıt =SaveData()
        bugun = str(datetime.datetime.today())

        if ((self.ad.get() == "") or (self.tc.get() == "") or (self.yas.get() == "") or (self.dogum_tarihi.get() == "") or (
                self.cv.get() == "") or (self.bolum.get() == "") or
                (self.ogrenci_gsm.get() == "") or (self.mail.get() == "") or (self.veli_ad.get() == "") or (
                        self.veli_gsm.get() == "") or
                (self.veli_address.get() == "")):

            messagebox.showinfo("durum", "Boş alanları doldurunuz..")


        else:
            og_kayıt.student_save(self.ad.get().capitalize(), self.tc.get().capitalize(), self.yas.get().capitalize(), self.dogum_tarihi.get(),
                        self.cv.get().casefold(), self.bolum.get().capitalize(),
                        self.ogrenci_gsm.get().capitalize(), self.mail.get().capitalize(), self.veli_ad.get().capitalize(), self.veli_gsm.get(),
                        self.veli_address.get(), bugun)


            print("Öğrenci başarılı bir şekilde kaydedildi\n")
            messagebox.showinfo("durum", "Öğrenci Başarılı bir şekilde kaydedildi..")

            self.destroy()



    def pencere_ac(self):
        self.mainloop()


    def getTc(self):
        return  self.tc_no


Admin()