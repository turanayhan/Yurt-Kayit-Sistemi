import xml.etree.ElementTree as ET

from datetime import date


def data_kaydet(ad_, tc_, yas_, dg_tarihi_, okul_, bolum_, gsm_, mail_,veli_ad_,veli_gsm_,veli_address_,kayit_tarihi_):
    data1 = ET.Element('data')
    data=ET.SubElement(data1 ,'Student')
    data.set('id', tc_)

    tc = ET.SubElement(data, 'Tc')
    ad = ET.SubElement(data, 'Ad')
    yas = ET.SubElement(data, 'Yas')
    dogum_tarihi = ET.SubElement(data, 'DogumTarihi')
    gsm = ET.SubElement(data, 'Gsm')
    mail = ET.SubElement(data, 'Mail')
    okul = ET.SubElement(data, 'Okul')
    bolum = ET.SubElement(data, 'Bolum')
    veli_ad = ET.SubElement(data, 'VeliAd')
    veli_gsm = ET.SubElement(data, 'VeliGsm')
    veli_address=ET.SubElement(data, 'VeliAddress')
    kayıt_tarihi=ET.SubElement(data, 'KayitTarihi')



    tc.text = tc_
    ad.text = ad_
    yas.text = yas_
    tc.text = tc_
    mail.text = mail_
    gsm.text=gsm_
    okul.text = okul_
    bolum.text = bolum_
    veli_ad.text = veli_ad_
    veli_gsm.text=veli_gsm_
    veli_address.text=veli_address_
    dogum_tarihi.text=dg_tarihi_
    kayıt_tarihi.text=kayit_tarihi_
    db = ET.tostring(data1)

    with open("data/Ogrenciler.xml", "ab") as f:

        f.write(db)

