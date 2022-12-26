from abc import ABC, abstractmethod


class İnsan(ABC):

    # Constructor
    def __init__(self, ad, tc, yas, dogum_tarihi):
        self.ad = ad
        self.tc = tc
        self.dogum_tarihi = dogum_tarihi
        self.yas = yas

    @abstractmethod
    def tam_isim(self):
        pass
