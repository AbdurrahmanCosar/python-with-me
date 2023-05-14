# BankAccount isminde bir sınıf tanımlayınız
# Üretilen her bir nesne owner isminde bir özellğe sahip olmalıdırBankAccount("Abduley")
# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır
# Üretilen her bir nesne için deposit metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp balance üzerine ekleyin ve balance miktarını geriye döndürün
# Üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance değerinden çıkarıp geriye döndürün

# hesap = BankAccount("Abduley")
# hesap.owner = Abduley
# hesap.balance => 0.0
# hesap.deposit(1000) => 1000.0
# hesap withdraw(500) => 500.0


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0


    def show_balance(self):
        return f"Hesabınızda {self.balance} TL var"

    def deposit(self, amount):

        self.balance += float(amount)
        return f"Yeni bakiyeniz: {self.balance}"
    
    def withdraw(self, amount):

        if float(amount) > self.balance:
            return "Yetersiz bakiye!"

        self.balance -= float(amount)
        return f"Yeni bakiyeniz: {self.balance}"
    
c = BankAccount("Abduley")

print(c.show_balance())
print(c.deposit(1000))
print(c.withdraw(500))