website = "https://www.gencyazilimci.com"
name = "  Abdurrahman Coşar  "

# 1 - name değişkenindeki baş ve sondaki boşlukları silin.
r = name.strip()

# 2 - website değişkenindeki gencyazilimci bilgisi haricindeki her karakteri silin.
r = website.strip("htps://www..com")

# 3 - website içinde kaç tane a karakteri vardır?
r = website.count("a")

# 5 - website "www" ile başlayıp bitiyor mu?
r = website.startswith("www")

# 6 - website içinde ".com" ifadesi var mı?
r = website.find(".com")

# 7 - "name" içindeki karakterlerin hepsi alfabetik mi?
r = name.isalpha()

# 8 - name değişkeninin satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
r = name.center(50, "*")
r = name.ljust(50, "*")
r = name.rjust(50, "*")

# 9 - name içinde tüm boşluk karakterlerini "-" ile değiştirin
r = name.replace(' ', '-')

# 10 - name içinde boşluk karakterlerinde ayrırın.
name = name.replace(" ", "-")

print( r)