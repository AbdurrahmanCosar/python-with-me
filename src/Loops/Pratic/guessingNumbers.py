import random 

number = random.randint(1, 100) 
# Başlangıç ve bitiş değerlerini veriyoruz ardından bizim için her çalıltığıda rastgele sayı oluşturuyor

right = int(input("Kaç hak ile oyuna başlamak istersiniz?: "))
hp = right
counter = 0

while hp > 5:
    hp -= 1
    counter += 1
    guess = int(input("Guess Number: "))

    if number == guess:
        print(f"Tebrikler {counter}. denemenizde doğru bildiniz. Toplam puanınız: {100 - (100 / right) * (counter - 1)}")
        break

    elif number > guess:
        print("Sayı, tahmin ettiğiniz sayıdan daha büyük.")

    else:
        print("Sayı, tahmin ettiğiniz sayıdan daha küçük.")

    if hp == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {number}")
        break