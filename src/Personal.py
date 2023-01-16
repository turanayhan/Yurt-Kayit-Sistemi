from src.Human import Human


class Personal(Human):
    def __init__(self,ad, tc, yas, dogum_tarihi,unvan,gorevi,mail):
        Human.__init__(self,ad,tc,yas,dogum_tarihi)
        self.__unvan=unvan
        self.__gorevi=gorevi
        self.__mail=mail

    def getUnvan(self):
        return self.__unvan

    def getGorevi(self):
        return self.__gorevi

    def getMail(self):
        return self.__mail