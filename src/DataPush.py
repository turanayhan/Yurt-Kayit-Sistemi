import xml.etree.ElementTree as ET


def data_regsiter(self, name_, age_, idenity_, gsm_, mail_, school_, section_, g_name_,g_gsm_,g_address_):
    data = ET.Element('Student')
    data.set('id', "1")

    idenity = ET.SubElement(data, 'Tc')
    name = ET.SubElement(data, 'Name')
    age = ET.SubElement(data, 'Age')
    gsm = ET.SubElement(data, 'Gsm')
    mail = ET.SubElement(data, 'Mail')
    school = ET.SubElement(data, 'School')
    section_name = ET.SubElement(data, 'Section')
    g_name = ET.SubElement(data, 'Gname')
    g_gsm = ET.SubElement(data, 'Ggsm')
    g_address=ET.SubElement(data, 'Gaddress')

    idenity.text = idenity_
    name.text = name_
    age.text = age_
    gsm.text = gsm_
    mail.text = mail_
    school.text = school_
    section_name.text = section_
    g_name.text = g_name_
    g_gsm.text=g_gsm_
    g_address.text=g_address_

    db = ET.tostring(data)

    with open("data/StudentsList.xml", "ab") as f:
        f.write(db)
