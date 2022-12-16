from src.Personal import Personal


class Student(Personal):

    # Constructor
    def __init__(self, name, surname, identification, age, date, experience):
        Personal.__init__(self, name, surname, identification, age, date)
        self.experience = experience

    def full_name(self):
        return f"{self.name} {self.surname}"
