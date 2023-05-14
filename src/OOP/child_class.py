class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person object was created")

    def say_hello(self):
        print("Hello" + self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        Person.__init__(self, name, surname, age)
        self.number = number
        print("Student object was created")
