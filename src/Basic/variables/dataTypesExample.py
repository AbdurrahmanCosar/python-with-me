'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    
    ** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)

pi = 3.14

r = float(input("half diameter: "))

area = pi * (r ** 2)
around = 2 * pi * r

result = "area: " + str(alan) + " around: " + str(cevre)
print(result)

'''

'''
    Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
'''

print("how many kilometers have you traveled?")
distanceKm = input()
distanceMile = float(distanceKm) / 1.609344
distanceMile = round(distanceMile, 2)

print(str(distanceKm) + " kilometers = " + str(distanceMile) + " miles.")
