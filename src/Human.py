from abc import ABC, abstractmethod


class Human(ABC):
    # Constructor
    def __init__(self, ad, tc, yas, dogum_tarihi):
        self.__ad = ad
        self.__tc = tc
        self.__dogum_tarihi = dogum_tarihi
        self.__yas = yas

    def getAd(self):
        return self.__ad

    def getTc(self):
        return self.__tc

    def getDt(self):
        return self.__dogum_tarihi

    def getYas(self):
        return self.__yas
