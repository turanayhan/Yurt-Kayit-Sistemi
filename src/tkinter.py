import tkinter
from tkinter import *

base = Tk()
base.geometry("800x800")
base.title("Öğrenci Kayıt Ekanı")

lb1 = Label(base, text="Öğrenci Ad Soyad :", width=15, font=("arial", 12), justify=tkinter.RIGHT)
lb1.place(x=20, y=50)
en1 = Entry(base)
en1.place(x=200, y=50)

lb3 = Label(base, text="Tc Kimlik no :", width=15, font=("arial", 12), justify=tkinter.RIGHT)
lb3.place(x=20, y=100)
en3 = Entry(base)
en3.place(x=200, y=100)

lb4 = Label(base, text="Öğrenci Yaşı :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb4.place(x=19, y=150)
en4 = Entry(base)
en4.place(x=200, y=150)

list_of_cntry = ("İnöü üniversitesi", "Turgut Özal Üniversitesi", "Fırat Üniveristesi", "Eskişehir Üniveristesi")
cv = StringVar()
drplist = OptionMenu(base, cv, *list_of_cntry)
drplist.config(width=15)
cv.set("Seç")
lb2 = Label(base, text="Kayıtlı üniversite :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb2.place(x=15, y=200)
drplist.place(x=200, y=200)

lb6 = Label(base, text="Okuduğu Bölüm :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb6.place(x=15, y=250)
en6 = Entry(base, show='*')
en6.place(x=200, y=250)

lb7 = Label(base, text="Telefon Numarası :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb7.place(x=15, y=300)
en7 = Entry(base, show='*')
en7.place(x=200, y=300)

lb8 = Label(base, text="Doğum Tarihi :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb8.place(x=15, y=350)
en8 = Entry(base, show='*')
en8.place(x=200, y=350)

lb9 = Label(base, text="E Posta Adresi  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb9.place(x=15, y=400)
en9 = Entry(base, show='*')
en9.place(x=200, y=400)

lb10 = Label(base, text="Veli Ad Soyad  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb10.place(x=15, y=450)
en10 = Entry(base, show='*')
en10.place(x=200, y=450)

lb11 = Label(base, text="Veli Telefon  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb11.place(x=15, y=500)
en11 = Entry(base, show='*')
en11.place(x=200, y=500)

lb11 = Label(base, text="Veli Adress  :", width=15, font=("arial", 12), justify=tkinter.LEFT)
lb11.place(x=15, y=550)
en11 = Entry(base, show='*')
en11.place(x=200, y=550)


def kaydet():
    ad = lb1.get()
    tc = lb2.get()


btKaydet = Button(base, text="Kaydet", command=kaydet, width=15, font=("arial", 12))
btKaydet.place(x=200, y=600)

base.mainloop()




