from abc import ABC, abstractmethod


class Contact(ABC):
    def __init__(self,gsm,mail):
        self.__gsm=gsm
        self.__mail=mail


    @abstractmethod

    def getGsm(self):
        return self.__gsm

    def getMail(self):

        return self.__mail
