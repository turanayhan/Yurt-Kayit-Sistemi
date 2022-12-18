import xml.etree.ElementTree as xml

veriler = xml.parse("data/StudentsList.xml")


kok = veriler.getroot()

for altseviye in kok:
  print(altseviye.tag,altseviye.attrib)

