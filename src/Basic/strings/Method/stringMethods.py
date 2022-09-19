msg = "  Hello everyone. My name is Abdurrahman. I'm currently learning Python  "

r = msg.upper() # Bütün mesajı büyük harfle yazdırır.
r = msg.lower() # Bütün mesajı küçük harfle yazdırır.
r = msg.title() # Her kelimenin ilk harfini büyük yazdırır.
r = msg.capitalize() # Sadece cümlenin ilk harfini büyük harfe çevirir.

r = msg.islower() # "Bütün harfler küçük mü?" sorgusunu sorarız
r = msg.istitle() # "Baş harfleri büyük mü?" sorgusunu sorarız

r = msg.strip() # Baş ve sondaki boşluk (" ") karakterlini sileriz.
r = msg.lstrip() # Baştaki boşluk (" ") karakterlini sileriz.
r = msg.rstrip() # Sondaki boşluk (" ") karakterlini sileriz.
r = msg.split() # Stringi böler. Herhangi bir değer vermezsek varsayılan olarak boşluklardan böler.
r = msg.split(".") # Noktalardan böler

r = r[0] # İlk stringi alır.

r = msg.split()
r = "-".join(r) # Dizideki bütün elemanların arasına - ekler.

index = msg.index("Abdurrahman") # Aramış olduğumuz kelimenin kaçıncı indexten başladığını alırız.

r = msg.startswith("H") # "H ile mi başlıyor?" sorgusunun sorarız ve True döner
r = msg.endswith("j") # "j ile mi bitiyor?" sorgusunun sorarız ve False döner

r = msg.replace("e", "E") # Küçük e karakterini büyük E ile değiştirir.


print(r)