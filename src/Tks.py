import tkinter
from tkinter import *
from src.OgrenciKayıt import OgrenciKayıt
import datetime

base = Tk()
base.geometry("400x800")
base.title("Öğrenci Kayıt Ekanı")

lb1 = Label(base, text="Öğrenci Ad Soyad :", width=15, font=("arial", 12), justify=tkinter.RIGHT)
lb1.place(x=20, y=50)
ad = Entry(base)
ad.place(x=200, y=50)

lb2 = Label(base, text="Tc Kimlik no :", width=15, font=("arial", 12), justify=tkinter.RIGHT)
lb2.place(x=20, y=100)
tc = Entry(base)
tc.place(x=200, y=100)

lb3 = Label(base, text="Öğrenci Yaşı :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb3.place(x=19, y=150)
yas = Entry(base)
yas.place(x=200, y=150)

list_of_cntry = ("İnöü üniversitesi", "Turgut Özal Üniversitesi", "Fırat Üniveristesi", "Eskişehir Üniveristesi")
cv = StringVar()
drplist = OptionMenu(base, cv, *list_of_cntry)
drplist.config(width=15)
cv.set("Seç")
lb4 = Label(base, text="Kayıtlı üniversite :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb4.place(x=15, y=200)
drplist.place(x=200, y=200)

lb5 = Label(base, text="Okuduğu Bölüm :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb5.place(x=15, y=250)
bolum = Entry(base)
bolum.place(x=200, y=250)

lb6 = Label(base, text="Telefon Numarası :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb6.place(x=15, y=300)
ogrenci_gsm = Entry(base)
ogrenci_gsm.place(x=200, y=300)

lb7 = Label(base, text="Doğum Tarihi :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb7.place(x=15, y=350)
dogum_tarihi = Entry(base)
dogum_tarihi.place(x=200, y=350)

lb8 = Label(base, text="E Posta Adresi  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb8.place(x=15, y=400)
mail = Entry(base)
mail.place(x=200, y=400)

lb9 = Label(base, text="Veli Ad Soyad  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb9.place(x=15, y=450)
veli_ad = Entry(base)
veli_ad.place(x=200, y=450)

lb10 = Label(base, text="Veli Telefon  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb10.place(x=15, y=500)
veli_gsm = Entry(base)
veli_gsm.place(x=200, y=500)

lb11 = Label(base, text="Veli Adress  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb11.place(x=15, y=550)
veli_address = Entry(base)
veli_address.place(x=200, y=550)


def kaydet():
    turan = OgrenciKayıt()
    bugun = str(datetime.datetime.today())

    turan.kayıt(ad.get().capitalize(),tc.get().capitalize(),yas.get().capitalize(),dogum_tarihi.get(), cv.get().casefold(), bolum.get().capitalize(),
                ogrenci_gsm.get().capitalize(),mail.get().capitalize(),veli_ad.get().capitalize(),veli_gsm.get(),
                veli_address.get(),bugun)
    print("Öğrenci başarılı bir şekilde kaydedildi\n")


btKaydet = Button(base, text="Kaydet", command=kaydet, width=15, font=("arial", 12))
btKaydet.place(x=200, y=600)


def pencere_ac():
    base.mainloop()


