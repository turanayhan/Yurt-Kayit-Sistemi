from src.StudentRegistration import StudentRegistration


def addStudent():
    turan = StudentRegistration()
    turan.register()
    print("Öğrenci başarılı bir şekilde kaydedildi")


def deleteStudent():
    pass


def callStudent():
    pass


def getStudentsList():
    pass


def studentUpdade():
    pass


while True:
    print("1-Öğrenci Ekle")
    print("2-Öğrenci sil")
    print("3-Temizlik Personeli Kayıt")
    print("4-Tümünü Listele")
    print("5-Güncelleme")

    secim = int(input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (0-7):"))

    if secim == 1:

        addStudent()

    elif secim == 2:

        deleteStudent()

    elif secim == 3:

        callStudent()

    elif secim == 4:

        getStudentsList()

    elif secim == 5:

        studentUpdade()

    else:
        print("Lütfen Geçerli bir sayı giriniz")
        continue
