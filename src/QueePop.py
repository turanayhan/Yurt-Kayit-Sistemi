from xml.etree.ElementTree import ElementTree
class Queepop:
  def __init__(self):
    self.tree = ElementTree()
    self.tree.parse('data/yedekler.xml')


  def delete_personal(self):
    personals = self.tree.findall('Öğrenciler')
    for personal in personals:
      childs = personal.findall(id)
      for child in childs:

        personal.remove(child)

    self.tree.write("data/database.xml", encoding="UTF-8")


