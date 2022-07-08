# String Slicing yani String Parçalama

msg = "You will become best python developer in the world!"
msgLength = len(msg)

print(len(msg)) # Kaç karakterlik bir string olduğunu öğreniriz.

print(msg(msgLength)) # Hata alırız. Çünkü 0'dan başladığı için index numarasını, karakter sayısının 1 eksiğini yapmanız gerekiyor.
print(msg(msgLength - 1)) # Hata almayız


print(msg[0:5]) # 0'dan başlar ve 4'e kadar alır. 0'dan başladığı için 4'e kadar alır.
print(msg[7:15]) # 7'den, 14'e kadar alır.
print(msg[:10]) # En baştan 10. indexe kadar gider. Tabii ki de 10. index dahil değil. 9'a kadar alır.
print(msg[10:]) # 10'dan başlayarak en sona kadar gider.
print(msg[-9:-1]) # Sağdan 9. indexten, sağdan 2.indexe kadar gider

print(msg[0:40:2]) # 0'dan, 40'a kadar 2 seferde 1 karakter alarak gider.
print(msg[0:40:3]) # 0'dan, 40'a kadar 3 seferde 1 karakter alarak gider.

print(msg[:]) # Bütün karakterleri alırız.
print(msg[::2]) # Bütün karakterleri 2 seferde 1 karakter alarak alırız.

print(msg[::-1]) # Stringi sağdan sola doğru ters çevirir.