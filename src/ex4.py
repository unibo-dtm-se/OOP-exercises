# Write a Python program to create a "Person" class. 
# Include fields like "name", "country", and "date of birth". 
#Implement a method to determine the person's "age".

from datetime import datetime

class Person:
    
    def __init__(self, name, country, date_of_birth):
        self.__name = name
        self.__country = country
        self.__date_of_birth = date_of_birth

    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    def age(self):
        dob = datetime.strptime(self.__date_of_birth, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - dob.year 
        return age

    def __str__(self):
        return f"Name: {self.__name}, Country: {self.__country}, Date of Birth: {self.__date_of_birth}"
    
    def __eq__(self, other):
        return other is not None and \
            isinstance(other, Person) and \
            self.__name == other.__name and \
            self.__country == other.__country and \
            self.__date_of_birth == other.__date_of_birth

if __name__ == '__main__':
    p = Person("John", "USA", "01/01/2000")
    print(p.age()) 
    print(p.name) 
    print(p.country) 
    print(p.date_of_birth)