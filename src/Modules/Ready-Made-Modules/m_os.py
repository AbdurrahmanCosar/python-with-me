import os # Bu şekilde modülü import ediyoruz

result = dir(os)

result = os.name # İşletim sisteminizin adını alırsınız nt = Windows

result = os.getcwd() # Bulunduğumuz dosyanın konumunu bize verir
os.mkdir("newdirectory") # Aynı dizin içerisinde "newdirectory" adında bir klasör oluşturur

os.chdir("C:\\") # Bu şekilde dizini değiştirebiliriz
# Eğer C:\\ yerine .. yazarsak bir üst dizine çıkmış oluruz
# ../.. 2 kere üst dizine çıkmış oluruz

os.makedirs("newdir/newfolder") # Bu fonksiyon ile iç içe klaösr oluşturabiliriz

# listeleme
result = os.listdir()

# Filtreleme
for folder in os.listdir():
    if folder.endswith('.py'):
        print(folder)

datetime_folder = os.stat("m_datetime.py") # Dosya hakkında bilgi alırız
result = datetime_folder.st_size/1024

import datetime

result = datetime.datetime.fromtimestamp(datetime_folder.st_ctime) # Oluşturulma Tarihi
result = datetime.datetime.fromtimestamp(datetime_folder.st_atime) # Son erişilme tarihi
result = datetime.datetime.fromtimestamp(datetime_folder.st_mtime) # Son değiştirilme tarihi 


os.system("notepad.exe") # Notepad dosyasını açarız
os.rename("newdirectory", "newfolder") # İsim değiştirme (eski, yeni)
os.rmdir("newfolder") # Klasörü sileriz
os.removedirs("newfolder/newfolder") # Alt dizin varsa bunu kullanırız


# PATH

path_result = os.path.abspath("m_os.py") # Dosyanın tam konumunu alıyoruz
path_result = os.path.dirname("C:/python/modules/m_os.py") # Tam konumu verilen dosyanın dizin ismini alıyoruz
path_result = os.path.dirname(os.path.abspath("m_os.py")) # Dosyanın tam yolunu bulup dizin ismini alır
path_result = os.path.exists("m_os.py") # Dosyanın varlığını sorgular -> bool
path_result = os.path.isdir("C:/python/modules") # Klasör mü, değil mi?
path_result = os.path.isfile("C:/python/modules/m_os.py") # Dosya mü, değil mi?

path_result = os.path.join("C:\\", "testfolder", "testfolder1") # Path oluşturma
path_result = os.path.split("C:\\testfolder") # Path'i böler C:\\, testfolder
path_result = os.path.splitext("m_os.py") # Dosyanın ismi ve uzantısını ayırır