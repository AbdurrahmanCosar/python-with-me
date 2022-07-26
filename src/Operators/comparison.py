# email, password => database

a, b, c, d = 6, 6, 17, 3

result = (a == b) # = olursa atama,  == olursa karşılaştırma yapmış oluruz.
result2 = (a != b) # a, b'ye eşit değil mi diye sorarız

print(result) # Eşit ise True, değil ise False döner
print(result2) # Eşit değil ise True, eşit ise False döner.

# Username and Password
enterUsername = str(input("Kullanıcı adı giriniz: "))
enterPassword = str(input("Şifre giriniz: "))

username = "abduley"
password = "12345"

r = (enterUsername == username)  # kullanıcının girdiği değer "abduley" e eşit ise True döner
rP = (enterPassword == password) # kullanıcının girdiği değer "12345" e eşit ise True döner
print(r) 
print(rP)

#  Büyüktür ve Küçüktür
x = 6
y = 5

result = (x > y) # x, y'den büyük ise True döner
result = (x >= y) # x, y'den büyük veya eşit ise True döner
result = (y < x) # y, x'den küçük ise True döner
result = (y <= x) # y, x'den küçük veya eşit ise True döner
print(result)


# True == 1 
print(int(True)) # True bilgisi aslında 1'e karşılık gelir
print(int(False)) # False bilgisi aslında 0'a karşılık gelir

print( True == 1 ) # True, 1'e eşit ise True döner
print( False == 0 ) # False, 0'a eşit ise True döner
print( True != 1 ) # True, 1'e eşit değil ise True, eşit ise False döner
print( False != 0 ) # False, 0'a eşit değil ise True, eşit ise False döner 

print ( False + True + 100) # 0 + 1 + 100 = 101
