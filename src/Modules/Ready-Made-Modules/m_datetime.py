from datetime import datetime


result = datetime.now() # Şu anın tarih ve saat bilgisini alırız
result = datetime.now().day # Şu anın gün bilgisini alırız

now = datetime.now() # datetime classındaki now() fonksiyonunu çağırıyoruz
now = datetime.today() # datetime classındaki today() fonksiyonunu çağırıyoruz (now ile aynı)

day = now.day
print(day)

month = now.month
print(month)

year = now.year
print(year)

hour = now.hour
print(hour)

minute = now.minute
print(minute)

second = now.second
print(second)

ctime = datetime.ctime(now) # Ctime fonksiyonuna porametre olarak şimdiki zamanı gönderiyoruz ve daha detaylı bilgi alıyoruz
strftime = datetime.strftime(now, "%X %m %Y") # tırak içerisinde bir formatlama yapıyoruz. %d = day %y = year Daha fazla detay için --> https://strftime.org/
print(strftime)

t = "13 January 2023 hour 10:20:49"
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")