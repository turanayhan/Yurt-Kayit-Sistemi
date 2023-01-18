from xml.etree.ElementTree import ElementTree

from src.DbPush import DbPush

#eğer yurtta kalan herhangi bir öğrenci silindiğinde eğer bekleyen varsa yurda kayıt yapılır, aynı zamanda kayıt yaptıktan sonra dosyadan çıkar
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



