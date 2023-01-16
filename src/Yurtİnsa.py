
class oda():
    def __init__(self,yatak_Sayisi,odaNo):
        self.odaNo=str(odaNo)
        self.yatakSayisi=str(yatak_Sayisi)
        self.kayitliler=[]
    def kayitliEkle(self,instc):
        self.kayitliler.append(str(instc))
        return 1
    def kayitliSil(self,instc):
        if str(instc) in self.kayitliler:
            self.kayitliler.remove(str(instc))
            return 1
        else:
            return -1
    def kapasitesi(self):
        return int(int(self.yatakSayisi)-len(self.kayitliler))
    def yatakSayisiarttir(self,ert):
        self.yatakSayisi=str(int(self.yatakSayisi)+int(ert))
        return 1
    def kkurulum(self,kayitlileR):
        self.kayitliler=kayitlileR
        return 1
    def kayitlimi(self,instc):
        return str(instc) in self.kayitliler
    def getThisOda(self):
        asew3001=[]
        asew3001.append(self.yatakSayisi)
        asew3001.append(self.odaNo)
        for cr453 in range(len(self.kayitliler)):
            asew3001.append(self.kayitliler[cr453])
        return asew3001



class yurt():
    def __init__(self,yurt_No):
        self.yurtNo=str(yurt_No)
        self.odalar=[]
    def insanEkle(self,instc):
        kapsul=[]
        for x in range(len(self.odalar)):
            kapsul.append(self.odalar[x].kapasitesi())
        self.odalar[kapsul.index(max(kapsul))].kayitliEkle(instc)
        return 1
    def kisilerGoster(self):
        for x in self.odalar:
            print(x.kayitliler)
        return 1
    def direkEkle(self,oda_no,instc):
        for i in range(len(self.odalar)):
            if self.odalar[i].odaNo==str(oda_no):
                self.odalar[i].kayitliEkle(instc)
                return 1
        return -1
    def getkisiler(self):
        ace=""
        for u in self.odalar:
            for t in u.kayitliler:
                ace+=t+"#"
            ace=ace[0:-1]
            ace+="$"
        q=ace[0:-1]
        return q
    def getodalar(self):
        acu=""
        for yo in self.odalar:
            acu+=yo.odaNo+"#"
        p=acu[0:-1]
        return p
    def odaEkle(self,oda):
        self.odalar.append(oda)
        return 1
    def insanSil(self,instc):
        for xq in range(len(self.odalar)):
            if self.odalar[xq].kayitlimi(instc):
                self.odalar[xq].kayitliSil(instc)
                return 1
        return 0
    def getThesepeoplewithhome(self):
        pekaci=[]
        for dew2312 in range(len(self.odalar)):
            pekaci.append(self.odalar[dew2312].getThisOda())
        return pekaci
    def yerVarmi(self):
        for han7 in self.odalar:
            if han7.kapasitesi()>0:
                return 1
        return 0



class Yurtinsa:
    def __init__(self,yurt_Adı,oda_no,yatak_sayısı):
        self.yurt=yurt(yurt_Adı)

        for x in range(len(oda_no)):
            self.yurt.odaEkle(oda(yatak_sayısı[x],oda_no[x]))





class Yks:
    def __init__(self,yurt):
        self.yurt=yurt

    def insan_ekle(self,tc):
        self.yurt.insanEkle(tc)

    def insan_sil(self,tc):
        self.yurt.insanSil(tc)

