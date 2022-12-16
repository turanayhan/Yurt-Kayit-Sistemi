from src.Personal import Personal


class Student(Personal):

    # Constructor
    def __init__(self, name, surname, identification, age, date):
        Personal.__init__(self, name, surname, identification, age, date)


    def full_name(self):
        return f"{self.name} {self.surname}"