from abc import ABC, abstractmethod


class Personal(ABC):

    # Constructor
    def __init__(self, name, surname, identification, age, date):
        self.name = name
        self.surname = surname
        self.identification_number = identification
        self.date_of_birth = date
        self.age = age

    @abstractmethod
    def full_name(self):
        pass
