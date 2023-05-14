class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def intro(self):
        print(self.name, self.surname, self.age)

    
class Student(Person):
    pass

class Teacher(Person):
    pass


p1 = Person("Abduley", "Dev", 17)
p1.intro()

s1 = Student("Pastel", "Software", 23)
s1.intro()

t1 = Teacher("Emre", "Phys", 17)
t1.intro()