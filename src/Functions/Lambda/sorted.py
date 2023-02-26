# Sorted() fonksiyonu sıralama işlemlerinde kullanılır
# Sorted fonksiyonu sözlüklerde kullanılabilir
# Asıl listeyi değiştirmez

numbers = [2,56,133,22,41,61,17,77,54]

result = sorted(numbers) # Sayıları default olarak küçükten büyüğe sıralar
result = sorted(numbers, reverse = True) # reverse = True dediğimiz zaman büyükten küçüğe doğru sıralar!


customers = [
    {"name": "abduley", "messages": ["msg1", "msg2", "msg3"], "email": "info@gencyazilimci.com"},
    {"name": "zehra", "messages": []},
    {"name": "tarik", "messages": ["msg1", "msg2"], "phone": "312313"}
]

result = sorted(customers, key = len)
# key parametresini boş bırakırsak neye göre sıralayacağını bilmediği için hata verir!
# key parametresine len referansını gönderdiğimiz zaman key uzunluğuna göre sıralar!

result = sorted(customers, key = lambda customer: customer["name"]) # customer isimlerini alfabetik olarak sıralar
result = sorted(customers, key = lambda customer: len(customer["messages"]), reverse = True) # customer mesaj sayılarını büyükten küçüğe

courses = [
    {"course_name": "C++", "student": 20000},
    {"course_name": "Java", "student": 16000},
    {"course_name": "Python", "student": 37000}
]

result = map(lambda c: c["course_name"], sorted(courses, key = lambda course: course["student"], reverse = True))
"""
sorted() fonksiyonu ile öğrenci kursların öğrenci sayılarını büyükten küçüğe doğru sıraladık
ilk lambda fonksiyonu ile öğrenci sayısı büyük olan kursun ismini aldık

"""

print(list(result))