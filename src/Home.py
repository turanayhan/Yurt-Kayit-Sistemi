from src.StudentRegistration import StudentRegistration


def addStudent():
    print("Öğrenci Kayıt Ekranı..\n")
    turan = StudentRegistration()
    turan.register()
    print("Öğrenci başarılı bir şekilde kaydedildi\n")
    menu()





def deleteStudent():
    pass


def callStudent():
    pass


def getStudentsList():
    pass


def studentUpdade():
    pass



def menu():
    while True:
        print("1-Öğrenci Ekle")
        print("2-Öğrenci sil")
        print("3-Temizlik Personeli Kayıt")
        print("4-Tümünü Listele")
        print("5-Güncelleme")

        secim = input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (0-7):\n")

        if secim == "1":

            addStudent()
            break

        elif secim == "2":

            deleteStudent()

        elif secim == "3":

            callStudent()

        elif secim == "4":

            getStudentsList()

        elif secim == "5":

            studentUpdade()

        else:
            print("\nMenu elemanlarından birini seçiniz...\n")
            continue


menu()
