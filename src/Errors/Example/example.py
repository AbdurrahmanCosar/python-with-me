my_list = ["1","5", "9a", "10b", "abc", "20", "44"]

# 1 -> Liste elemanları içindeki sayısal değerleri bulunuz.

numbers = '\n'.join(i for i in my_list if i.isdigit())
print(numbers)

# 2 -> Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz
# aksi halde hata mesajı yazdırınız

while True:
    x = input("harf giriniz ")
    if x == 'q':
        break

    y = input("sayı giriniz: ")

    try:
        y = int(y)
        print("Girdiğiniz sayı {}".format(y))
    except ValueError:
        print("y bir sayı olmalıdır")
        continue

# 3 -> Dict ve key bilgilerini parametre olarak alan get(d, key) fonksiyonunu hazırlayınız
# d= {"product_name": "iphone"}
# d["price"] => keyError
# get(d, "price") => None
# get(d, "product_name") => iphone

d = {"product_name" : "iphone"}

def get(dictionary, key):
    
    try:
        return dictionary.get(key)
    except KeyError:
        return None

print(get(d, "price"))