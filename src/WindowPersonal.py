import tkinter
from tkinter import *
from tkinter import messagebox
from src.SaveData import SaveData
import datetime


class WindowPersonal(tkinter.Tk):

    def __init__(self):

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





