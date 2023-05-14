class Person:

    # yapıcı metotlar (constructor)
    def __init__(self, name, surname, year):

        #object attributes, instance attributes
        self.name = name
        self.surname = surname
        self.year = year


    # instance methods
    def intro(self):
        return f"Adım {self.name} soyadım {self.surname}"
    
    def calculate_age(self):
        return f"{2023 - self.year} yaşındayım"
    
# Object, Instance
p1 = Person("Abdurrahman", "Coşar", 2000)

print(p1.intro())
print(p1.calculate_age())