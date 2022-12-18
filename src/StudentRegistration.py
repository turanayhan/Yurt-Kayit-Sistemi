from src import DataPush
from src.Guardian import Guardian
from src.Student import Student


class StudentRegistration(object):

    def __init__(self):
        self.student = Student("", "", "", "", "", "", "", "", "")
        self.guardian = Guardian("", "", "", "")

    def register(self):
        name = input("Adınız : ")
        surname = input("Soyadınızı: ")
        identification = input("Tc kimlik: ")
        age = input("Yaşınız: ")
        date = input("Doğum tarihiiniz: ")
        school = input("Okulunuz: ")
        section_name = input("Okuduğunuz Bölümün: ")
        student_gsm = input("Telefon Numarası: ")
        mail = input("e posta adresini giriniz: ")

        self.student = Student(name, surname, identification, age, date, school, section_name, student_gsm, mail)

        guardian_name = input("Veli Adı: ")
        guardian_surname = input("Veli Soyad: ")
        guardian_gsm = input("Veli Telefon: ")
        guardian_address = input("Veli Address: ")

        self.guardian = Guardian(guardian_name, guardian_surname, guardian_gsm, guardian_address)

        self.set_data(self.student, self.guardian)

    def getStudent(self):
        print(f'{self.student.name}\n{self.student.surname}\n'
              f'{self.student.age}\n{self.student.date_of_birth}\n'
              f'{self.student.school}\n{self.student.surname}\n'
              f'{self.student.identification_number}\n{self.guardian.g_name}\n'
              f'{self.guardian.g_surname}\n{self.guardian.g_gsm}\nt')

    def set_data(self, student, guardian):

        students= DataPush
        students.data_regsiter(student.full_name(),student.age,student.identification_number,student.gsm,student.mail,student.school,student.section_name,"ibo","sagvs")


