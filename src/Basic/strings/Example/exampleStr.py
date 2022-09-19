website = "https://www.gencyazilimci.com"
repoName = "Python with Me"

#* 1- 'repoName' karakter dizisinde kaç karakter bulunmaktadır?
print(len(repoName))

#* 2 - 'website' içinden www karakterlerini alınız.
print(website[8:11])

#* 3 - 'website' içinden com karakterlerini alınız.
print(website[-3:])

#* 4 - 'repoName' içinden ilk 9 ve son 9 karakteri alın.
print(repoName[:10]) # ilk 9
print(repoName[-10:]) # son 9

#* 5 - 'repoName' ifadesindeki karakterleri tersten yazdırın.
print(repoName[::-1])

#* 6 - 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s)

#* 7 - 'abc' ifadesini yan yana 3 defa yazdırın.
print("abc" * 3)

name, surname, age, job = "Abdurrahman", "Coşar", 17, "Student"

#* 9 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# "Benim adım Mehmet Çetin, Yaşım 34 ve mesleğim mimar."
name, surname, age, job = "Mehmet", "Çetin", 34, "Mimar"
print("Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name, surname, age, job))