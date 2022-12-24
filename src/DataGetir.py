import xml.etree.ElementTree as xml
from datetime import date
veriler = xml.parse("data/Ogrenciler.xml")


kok = veriler.getroot()

for altseviye in kok:
  print(altseviye.tag,altseviye.attrib)


today = date.today()
print("Bugünün Tarihi:", today)

