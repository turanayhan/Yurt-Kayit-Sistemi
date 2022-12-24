class Veli:

    def __init__(self, veli_ad, veli_soyad, veli_gsm, veli_address):
        self.veli_ad = veli_ad
        self.veli_soyad = veli_soyad
        self.veli_address = veli_address
        self.veli_gsm = veli_gsm

    def full_name(self):
        return f"{self.veli_ad} {self.veli_soyad}"
