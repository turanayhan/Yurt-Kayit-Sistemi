import xml.etree.ElementTree as xml
from src.Personal import Personal
from src.Student import Student


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



