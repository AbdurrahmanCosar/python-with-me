class User: 

    active_users = 0 #

    @classmethod # Bir decorator oluşturuyoruz. İlerleyen zamanlarda öğreneceğiz
    def display_active_users(cls):
        print(cls)

    @classmethod
    def from_string(cls, data_str): # Bu şekilde de bir nesne oluşturabiliriz
        first, last, age = data_str.split(",")
        return cls(first, last, age)

    def __init__(self, first, last, age ):
        self.first = first
        self.laste = last
        self.age = age

        User.active_users += 1 

    def logout(self):
        User.active_users -= 1
        return f"{self.first} {self.last} uygulamadan çıkış yaptı"
    
User.from_string("Abdurrahman,Coşar,17") 