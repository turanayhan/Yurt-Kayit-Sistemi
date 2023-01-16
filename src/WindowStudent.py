import tkinter
from tkinter import *
from tkinter import messagebox
from src.SaveData import SaveData
import datetime

class WindowStudent(tkinter.Tk):

    def __init__(self):
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



