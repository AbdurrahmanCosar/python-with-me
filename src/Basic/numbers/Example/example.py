"""
    Uygulama 1: Bir öğrencinin aşağıdaki bilgileri için gerekli değişkenleri oluşturunuz.
    Öğrenci adı
    Öğrenci soyadı
    Öğrenci ad + soyad
    Öğrenci numarası
    Öğrenci cinsiyet
    Öğrenci tc kimlik
    Öğrenci doğum yılı
    Öğrenci adres bilgisi   
    Öğrenci yaşı 
"""

studentName = 'Abdurrahman'
studentSurname = 'Cosar'
studentNameAndSurname = studentName +' '+ studentSurname
print(studentNameAndSurname)

studentGender = True  # Male
print(studentGender)

studentGender = False # Female
print(studentGender)

studentID = "12345678900"
studentDateOfBirth = 2017

studentAge = 2021 - studentDateOfBirth
print(studentAge)

studentAddress = 'Konya Meram'


"""
    Uygulama 2: Aşağıdaki ürünlerin toplam bilgisini hesaplayınız.
    
    Ürün 1 => 50     TL - Turkish Lira
    Ürün 2 => 60.5   TL - Turkish Lira
    Ürün 3 => 356.45 TL - Turkish Lira
"""

product1 = 50
product2 = 60.5
product3 = 356.45

total = product1 + product2 + product3
print("Total Product:", total)
