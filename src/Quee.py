class DbPush:
    def __init__(self):
        pass

    def student_kaydet(self, ad_, tc_, yas_, dg_tarihi_, okul_, bolum_, gsm_, mail_, veli_ad_, veli_gsm_, veli_address_,
                    kayit_tarihi_):
        studentData = ET.parse("data/yedekler.xml")
        # En üst seviye XML etiketinin ne olduğunu bulalım
        kok = studentData.getroot()
        # Eleman eklemek
        for ogrenciler in kok.findall("Öğrenciler"):
            ogrenci = ET.SubElement(ogrenciler, f'id{tc_}')
            tc = ET.SubElement(ogrenci, 'Tc')
            ad = ET.SubElement(ogrenci, 'Ad')
            yas = ET.SubElement(ogrenci, 'Yas')
            dogum_tarihi = ET.SubElement(ogrenci, 'DogumTarihi')
            gsm = ET.SubElement(ogrenci, 'Gsm')
            mail = ET.SubElement(ogrenci, 'Mail')
            okul = ET.SubElement(ogrenci, 'Okul')
            bolum = ET.SubElement(ogrenci, 'Bolum')
            veli_ad = ET.SubElement(ogrenci, 'VeliAd')
            veli_gsm = ET.SubElement(ogrenci, 'VeliGsm')
            veli_address = ET.SubElement(ogrenci, 'VeliAddress')
            kayıt_tarihi = ET.SubElement(ogrenci, 'KayitTarihi')

            #değerleri atıyoruz

            tc.text = tc_
            ad.text = ad_
            yas.text = yas_
            tc.text = tc_
            mail.text = mail_
            gsm.text = gsm_
            okul.text = okul_
            bolum.text = bolum_
            veli_ad.text = veli_ad_
            veli_gsm.text = veli_gsm_
            veli_address.text = veli_address_
            dogum_tarihi.text = dg_tarihi_
            kayıt_tarihi.text = kayit_tarihi_
            studentData.write("data/yedekler.xml", encoding="UTF-8")


    def Personal_kaydet(self,ad_, tc_, yas_, dg_tarihi_, unvan_,gorevi_,mail_):
        personalData = ET.parse("data/yedekler.xml")
        # En üst seviye XML etiketinin ne olduğunu bulalım
        kok = personalData.getroot()

        for ogrenciler in kok.findall("Personeller"):
            ogrenci = ET.SubElement(ogrenciler, f'id{tc_}')
            tc = ET.SubElement(ogrenci, 'Tc')
            ad = ET.SubElement(ogrenci, 'Ad')
            yas = ET.SubElement(ogrenci, 'Yas')
            dg_tarihi = ET.SubElement(ogrenci, 'DogumTarihi')
            unvan = ET.SubElement(ogrenci, 'Unvan')
            gorevi = ET.SubElement(ogrenci, 'Gorevi')
            mail = ET.SubElement(ogrenci, 'Mail')

            tc.text = tc_
            ad.text = ad_
            yas.text = yas_
            dg_tarihi.text = dg_tarihi_
            mail.text = mail_
            unvan.text=unvan_
            gorevi.text=gorevi_
            personalData.write("data/yedekler.xml", encoding="UTF-8")
