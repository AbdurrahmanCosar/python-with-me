# WHILE = KOŞUL

while True: # while True olduğu sürece uygulamak çalışacak. Burada sonsuz döngüye girer ve uygulama hata verir.
	print("Hello")

i = 0

while i < 10: # i 10'dan küçük olduğu sürece uygulamak çalışacak
	i += 1 # Her döndüğünde i'ye +1 ekliyoruz
	print(i) # 0'dan 9'a kadar gider


x = 1

while x <= 100: # x 100'e eşit olana kadar döngü çalışır
	if (x % 2 == 1): # while döngüsü içerisinde koşul belirtebiliriz
		print("Tek sayı: ", x)
	x += 1  """Eğer bunu if bloğunun içine yazarsak çift sayılarda 1 artmayacağı için program yine sonsuz döngüye girer ve hata verir"""

username = ''

print(bool(username)) # Eğer username değişkeni boş olursa yani '' olursa False, ' ' veya 'a' olursa True döner

while not username: # username'in içerisinde bir karakter olmadığı sürece yani False olduğu sürece burası çalışır
	username = input("Kullanıcı Adınız: ")
print("Kullanıcı adınız: ", username) 
