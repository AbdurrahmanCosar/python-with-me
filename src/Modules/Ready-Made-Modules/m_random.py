import random

value = dir(random)
value = help(random)

name = ["Ahmet", "Faruk", "Celal"]

result = random.choice(name) # Listeden rastgele bir eleman çeker
result = random.randint(1,10) # 1 ile 10 arasında rastgele bir sayı oluşturur


liste = list(range(10)) # 0 ile 10 arasında sayıların bulunduğu bir liste
random.shuffle(liste) # Listedeki elemanların yerlerini değiştirir

liste = list(range(100))
result = random.sample(liste, 3) # Belirtilen listeden rastgele 3 sayı alır