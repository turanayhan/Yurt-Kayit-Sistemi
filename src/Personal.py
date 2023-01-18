from src.Contact import Contact
from src.Human import Human

#personal sınıfı hem insandan hem iletişim sınıfından kalıtım alıyor aynı zamanda çoklu kalıtım yapıyoruz
class Personal(Human, Contact):
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
