from src.Contact import Contact
from src.Human import Human

# İnsan ve veli sınıfından miras alıyor
class Student(Human,Contact):

    # Constructor
    def __init__(self, ad="", tc="", yas="", dogum_tarihi="", okul="", bolum="", gsm="", mail="",veli_ad="",veli_gsm="",veli_address="", kayit_tarihi=""):
        Human.__init__(self, ad, tc, yas, dogum_tarihi)
        Contact.__init__(self,gsm,mail)
        self.__veli_ad=veli_ad
        self.__veli_gsm=veli_gsm
        self.__gsm2=gsm
        self.__veli_address=veli_address
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








