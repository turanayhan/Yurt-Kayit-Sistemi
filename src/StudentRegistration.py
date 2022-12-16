from src.Guardian import Guardian
from src.Student import Student


class StudentRegistration(object):

    def __init__(self):
        self.student = Student("", "", "", "", "", "", "")
        self.guardian = Guardian("", "", "", "")

    def register(self):
        name = input(print("Adınız: "))
        surname = input(print("Soyadınızı: "))
        identification = input(print("Tc kimlik: "))
        age = input(print("Yaşınız: "))
        date = input(print("Doğum tarihiiniz: "))
        school = input(print("Okulunuz: "))
        section_name = input(print("Okuduğunuz Bölümün: "))
        student_gsm = input(print("Telefon Numarası: "))
        mail = input(print("e posta adresini giriniz: "))

        self.student = Student(name, surname, identification, age, date, school, section_name, student_gsm, mail)

        guardian_name = input(print("Veli Adı: "))
        guardian_surname = input(print("Okuveli Soyad: "))
        guardian_gsm = input(print("Veli Telefon: "))
        guardian_address = input(print("Veli Address: "))

        self.guardian = Guardian(guardian_name, guardian_surname, guardian_gsm, guardian_address)

        self.getStudent()

    def getStudent(self):
        print(f'{self.student.name}\n{self.student.surname}\n'
              f'{self.student.age}\n{self.student.date_of_birth}\n'
              f'{self.student.school}\n{self.student.surname}\n'
              f'{self.student.identification_number}\n{self.guardian.g_name}\n'
              f'{self.guardian.g_surname}\n{self.guardian.g_gsm}\nt')


turan = StudentRegistration()

turan.register()
