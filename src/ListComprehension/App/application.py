students = ["Mahmut", "Caner", "Niyazi", "Berkay"]
string = "Hi User: 12513123!"
years = [1983, 1999, 1998, 2003]
degrees = [20, 5, 15, -2, 0, -6]

#* 1 - ) "1 - 100" arasındaki sayılardan 12'e tam bölünebilen sayı listesini oluşturunuz.

nums = [ i for i in range(1, 100) if i % 12 == 0 ]
print(nums)


#* 2 - ) "students" listesindeki her ismi küçük harfe çevirip tersten yazdırınız.

students = [i.lower()[::-1] for i in students]
print(students)

#* 3 - ) "years" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.

current_year = 2022

years = [f"Doğum Yılı: {year} - Yaş: {current_year - year}" for year in years]
print(years)

#* 4 - ) verilen "string" içindeki rakamları içeren bir liste oluşturunuz.

string = [int(l) for l in string if l.isnumeric()]
print(string)

#* 5 * ) "degrees" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yazınız

degrees = [f"Bugün hava {degree} derece"  if degree > 0 else f"Bugün hava {degree} derece. Dikkat Buzlanma Tehlikesi!" for degree in degrees]

degrees = "\n".join(degrees)
print(degrees)