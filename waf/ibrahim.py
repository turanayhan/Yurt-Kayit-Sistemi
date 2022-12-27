from abc import ABC, abstractmethod


class BankProducts(ABC):

    @abstractmethod
    def paraCek(self):
        pass

    @abstractmethod
    def paraYatir(self):
        pass

    @abstractmethod
    def bakiye(self):
        pass

    @abstractmethod
    def cikis(self):
        pass

    @abstractmethod
    def paraGonder(self):
        pass

    @abstractmethod
    def menu(self):
        pass

    @abstractmethod
    def program(self):
        pass

    @abstractmethod
    def adres(self):
        pass


class krediKarti(BankProducts):

    def __init__(self, adSoyad, tc, faturaAdres, nakitAvans, taksitSayisi, limit, bagliHesap, ekstreTarih, segment,
                 kartsifre):
        self.nakitAvans = nakitAvans
        self.taksitSayisi = taksitSayisi
        self.limit = limit
        self.bagliHesap = bagliHesap
        self.ekstreTarih = ekstreTarih
        self.segment = segment
        self.adSoyad = adSoyad
        self.tc = tc
        self.faturaAdres = faturaAdres
        self.kartsifre = kartsifre

    def paraCek(self):
            pass


    def paraYatir(self):
            pass


    def bakiye(self):
            pass


    def cikis(self):
            pass


    def paraGonder(self):
            pass


    def menu(self):
            pass


    def program(self):
            pass


    def adres(self):
            pass

class bankKart(BankProducts):

    def __init__(self, adSoyad, bakiye, hesapNo, tc, faturaAdres, kartsifre):
        self.adSoyad = adSoyad
        self.bakiye = bakiye
        self.hesapNo = hesapNo
        self.tc = tc
        self.faturaAdres = faturaAdres
        self.kartsifre = kartsifre

    def paraCek(self):
        pass

    def paraYatir(self):
        pass

    def bakiye(self):
        pass

    def cikis(self):
        pass

    def paraGonder(self):
        pass

    def menu(self):
        pass

    def program(self):
        pass

    def adres(self):
        pass


dosya = open("data.txt","r",encoding="utf-8")
oku = int(dosya.read())



dosya = open("bilgiler.txt","r",encoding="utf-8")
bankKart1 = bankKart(dosya.readline(), oku, dosya.readline(), dosya.readline(), dosya.readline(), dosya.readline())
print(bankKart1.adSoyad)

krediKarti1 = krediKarti("İbrahim Çayır", "51466", "malatya", 0, 5, 3000, "010", "10-10", "gold", "123456")
print(krediKarti1.faturaAdres)

takilanKart = bankKart1


class islem(BankProducts):
    def __init__(self, ad):
        self.ad = ad
        self.girisKontrol()
        self.dongu = True



    def girisKontrol(self):
        hak = 2
        for i in range(0, 3):
            sifre = input("lütfen sifrenizi giriniz: ")
            if sifre == takilanKart.kartsifre:
                self.program()
            elif sifre != takilanKart.kartsifre and hak != 0:
                hak -= 1
            elif sifre != takilanKart.kartsifre and hak == 0:
                print("kartınız bloke oldu en yakın şubeye başvurunuz!!")
                exit()

    def bakiye(self):
        print("hesap bakiyesi: {}".format(takilanKart.bakiye))
        self.dongu = False

    def paraGonder(self):
        gonderMiktar = float(input("gönderilecek miktar: "))
        if gonderMiktar < takilanKart.bakiye:
            yeniBakiye = takilanKart.bakiye - gonderMiktar
            dosya = open("data.txt", "w", encoding="utf-8")
            dosya.write(str(yeniBakiye))
        elif gonderMiktar > takilanKart.bakiye:
            print("Yetersiz bakiye")
        self.dongu = False

    def paraCek(self):

        miktar = int(input("lütfen çekeceğiniz miktarı giriniz:"))
        yeniMiktar = takilanKart.bakiye - miktar
        dosya = open("data.txt", "w", encoding="utf-8")
        dosya.write(str(yeniMiktar))
        if miktar > takilanKart.bakiye:
            print("yetersiz bakiye ")
            self.menu()
        else:
            print("hesabınızda kalan tutar: {}".format(yeniMiktar))
        self.dongu = False

    def paraYatir(self):
        miktar = int(input("Paranızı yatırınız"))
        yeniMiktar = takilanKart.bakiye + miktar
        dosya = open("data.txt", "w", encoding="utf-8")
        dosya.write(str(yeniMiktar))
        print("Bakiyeniz: {}".format(yeniMiktar))
        self.dongu = False

    def cikis(self):
        exit()

    def adres(self):
        print("Adres: {}".format(takilanKart.faturaAdres))

    def program(self):

        secim = self.menu()

        if secim == 1:
            self.bakiye()
        elif secim == 2:
            self.paraCek()
        elif secim == 3:
            self.paraYatir()
        elif secim == 4:
            self.paraGonder()
        elif secim == 5:
            self.adres()
        else:
            self.cikis()

    def menu(self):
        secim = int(input(
            "{} isimli {} hesap nolu yapmak istediğiniz işlemi seçiniz. \n[1]Bakiye sorgulama\n[2]para çek\n[3]para yatır\n[4]para gönder\n[5]adres\n[6]çıkış\n".format(
                takilanKart.adSoyad, takilanKart.hesapNo)))
        while secim < 1 or secim > 6:
            self.program()
        return secim


yeni = islem("a")
while yeni.dongu:
    yeni.program()
