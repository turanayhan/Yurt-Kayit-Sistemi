from xml.etree.ElementTree import ElementTree

from src.QueePop import QueePop


class DeleteData:
  def __init__(self):
    self.tree = ElementTree()
    self.tree.parse('data/database.xml')


  def delete_personal(self,tc_kimlik):
    id = f'id{tc_kimlik}'
    personals = self.tree.findall('Personeller')
    for personal in personals:

      childs = personal.findall(id)
      for child in childs:

        personal.remove(child)

    self.tree.write("data/database.xml", encoding="UTF-8")


  def delete_student(self,tc_kimlik):
    id = f'id{tc_kimlik}'
    students = self.tree.findall('Öğrenciler')
    for personal in students:
      childs = personal.findall(id)
      for child in childs:
        personal.remove(child)

    self.tree.write("data/database.xml", encoding="UTF-8")
    QueePop().kuyruktan_sil()
    print("yedek listesinden asil kayıt yapıldı")









