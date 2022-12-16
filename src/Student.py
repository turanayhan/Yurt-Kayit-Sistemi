from src.Personal import Personal


# Personal sınıfından miras alıyor
class Student(Personal):

    # Constructor
    def __init__(self, name, surname, identification, age, date, school, section_name, gsm, mail):
        Personal.__init__(self, name, surname, identification, age, date)
        self.school = school
        self.gsm = gsm
        self.mail = mail
        self.section_name = section_name

    def full_name(self):
        return f"{self.name} {self.surname}"
