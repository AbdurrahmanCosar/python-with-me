name = "Abdurrahman"
surname = "Cosar"
age = 17

print('My name is {}'.format(name)) # {} yerine name değişkenini koyar.

print('My name is {} {}'.format(name, surname)) # Birinci parametre yerine name, ikinci parametre yerine surname değişkenini koyar

print('My name is {0} {1}'.format(name, surname)) # Birinci parametre yerine name, ikinci parametre yerine surname değişkenini koyar
print('My name is {1} {0}'.format(name, surname)) # 1 yerine surname, 0 yerine name yazdırır.

print("My name is {n} {s}.".format(n=name, s=surname)) # Takma ad kullanabiliriz.


print("My name is {} {}. I'm {} years old.".format(name, surname, age))
print("My name is {} {}. I'm {} years old. {}".format(name, surname, age, age)) # Birden fazla kez kullanacağımız zaman tekrar ekleyebilir veya takma ad kullanarak daha rahat yapabiliriz

