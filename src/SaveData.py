from src.Personal import Personal
from src.DbPush import DbPush
from src.Quee import Quee
from src.Student import Student


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



