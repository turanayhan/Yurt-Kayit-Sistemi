from xml.etree.ElementTree import ElementTree

from src.QueePop import QueePop

#xml içerisindeki verileri girdiğimiz bilgilere göre silme
class DeleteData:
  def __init__(self):
    self.tree = ElementTree()
    self.tree.parse('data/database.xml')


  def delete_personal(self,tc_kimlik):
    #tc kimlik numarasına göre personal silme yapan kısım
    id = f'id{tc_kimlik}'
    personals = self.tree.findall('Personeller')
    for personal in personals:

      childs = personal.findall(id)
      for child in childs:

        personal.remove(child)

    self.tree.write("data/database.xml", encoding="UTF-8")
    print("Personel kaydı silindi..")


  def delete_student(self,tc_kimlik):
    # tc kimlik numarasına göre öğrenci silme yapan kısım
    id = f'id{tc_kimlik}'
    students = self.tree.findall('Öğrenciler')
    for personal in students:
      childs = personal.findall(id)
      for child in childs:
        personal.remove(child)

    self.tree.write("data/database.xml", encoding="UTF-8")
    print("Öğrenci kaydı silindi..")
    QueePop().kuyruktan_sil()
    print("yedek listesinden yeni öğrenci eklendi..")









