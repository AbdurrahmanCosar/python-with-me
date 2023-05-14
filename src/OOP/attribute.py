class User: 

    active_users = 0 # Sınıf seviyesinde bir değişken tanımlıyoruz ->Attribute

    def __init__(self, first, last, age ):
        self.first = first
        self.laste = last
        self.age = age

        User.active_users += 1 
        # init metodu her nesne üretildiğinde çalıştığı için 
        # her nesne üretildiğinde active_users bilgisi 1 artacak

    def logout(self):
        User.active_users -= 1
        return f"{self.first} {self.last} uygulamadan çıkış yaptı"
    




print(User.active_users)
userA = User("Abdurrahman", "Coşar", 17)
userB = User("Ravzanur", "Coşar", 7)
print(User.active_users)
userB.logout()
print(User.active_users)