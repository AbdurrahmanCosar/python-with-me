# 1 - Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
x  = int(input("Sayı : "))
print((x >50) and (x < 100))

# 2 - Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz
x  = int(input("Sayı : "))
print((x > 0) and (x%2 != 0))

# 3 - Username ve Parola ile giriş kontrolü yapınız
username_  = str(input("Username : "))
password_  = str(input("Password : "))

username = "abduley"
password = "1234"

print((username == username_) and (password == password_))

# 4 - Girilen 3 sayıyı büyük olarak karşılaştırın.
x  = int(input("Sayı : "))
y  = int(input("Sayı : "))
z  = int(input("Sayı : "))

result = (x>y) and (x>z) # x en büyük
print("x en büyük")

result = (y>x) and (y>z) # y en büyük
print("y en büyük")

result = (z>y) and (z>x) # z en büyük
print("z en büyük")

