names = ["Ada", "Yiğit", "Hasan", "Murat"]
ages = [2001, 2005, 1998, 2001]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")

# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")

# 3- "Yiğit" ismini listeden siliniz.
names.remove("Yiğit")

# 4- "Murat" isminin indexi nedir?
names.index("Murat")

# 5- Liste elemanlarını ters çevirin.
names.reverse()
ages.reverse()

# 6- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
ages.sort()

# 7- ages listesini rakamsal büyüklüğe göre sıralayınız.
ages.sort()

# 8- str = "iPhone X, iPhone XR" karakter dizisini listeye çeviriniz.
phones = "iPhone X, iPhone XR".split(",")

# 9- ages listesinin en büyük ve en küçük elemanı nedir?
min(ages) # En küçük
max(ages) # En büyük

# 10- ages listesinde kaç tane 2001 değeri vardır?
ages.count(2001)

# 11- "Beril" listenin bir elemanı mıdır?
response = "Beril" in names
print(response)

# 12- ages listesinin tüm elemanlarını siliniz.
ages.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []
marka = str(input(("1.Marka: ")))
markalar.append(marka)
marka = str(input(("2.Marka: ")))
markalar.append(marka)
marka = str(input(("3.Marka: ")))
markalar.append(marka)

