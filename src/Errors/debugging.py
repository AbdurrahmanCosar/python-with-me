import pdb # Python Debug kütüphanesini çapırıyoruz

one = "one"
two = "two"

pdb.set_trace()


# Eğer sonuc değişkenini yazarsak not defined hatası verir
# l yazark bütün satırları ve nerede olduğumuzu görürüz
# n ile sonraki satıra geçeriz. Eğer bulunduğumuz satır sonuc değişkeninin altında ise hata vermez ve yazdırır
# c ile tüm kodu çalıştırabiliriz
# p komutu p  one şeklinde kullanılır. İlgili değişkenin içeriğini verir

sonuc = one + two

three = "three"

sonuc += three

print(three)

# ---------------

def add_numbers(a, b, c):
    import pdb; pdb.set_trace() # bu şekilde tek satırda da import edebiliriz.
    return a + b + c

add_numbers(1, 2, 3) 






# l => list
# n => next line
# p => print
# c => continue
