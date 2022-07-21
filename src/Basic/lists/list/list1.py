sampleList = [] # Listeleri bu şekilde tanımlıyoruz

myList = [1, 3, 5, 7, 9] # Sayı listesi

response = myList # Listeyi yazdırırız
response = myList[0] # 0. elemanı yazdırır

teachers = ["Jimmy", "Micheal", "Jeff"]
print(type(teachers[0]))

userAbduley = ["Abduley", 17] # Listelerin içersinde tek bir tür olması gerekmiyor.
print(userAbduley[0])
print(userAbduley[1])

student1 = ["Abdurrahman", 17]
student2 = ["Mustafa", 15]

students =  [["Abdurrahman", 17], ["Mustafa", 15]] # Liste içinde liste oluşturabiliriz.
students2 = [student1, student2] # Başka listeleri bu şekilde tek bir liste içerisine toplayabiliriz.


response = students[0] # Abdurrahman'ın olduğu liste gelir.
response = students[1] # Mustafa'nın olduğu liste gelir.
response = students[0][0] # Abdurrahman'nın ismini alır.
response = students[1][0] # Mustafa'nın ismini alır.




print(response)
