name = "Abdurrahman" # String
surname = "cosar" # String
age = "17" # String
id = "452143215465245123" # ID, Kimlik No vs. String değerdir.

chars = "a" # Tek karakterler Python'da string olarak geçer. Fakat diğer dillerde "char" olarak geçer.

message = "My name is " + name + ". My surname is " + surname + ". I'm " + age + " years old."
# Stringler, Stringler ile işleme sokulabilir.


print(message)
print(type(name)) 

###

print(message[0]) # Karakter dizisi içerisinden ilk elemanı alır
print(message[-1]) # Karakter dizisi içerisinden son elemanı alır


# NOTE:
"""
    'I'm Abdurrahman' - FALSE
    "I'm Abdurrahman" - TRUE
    
    "This is "test" " - FALSE
    'This is "test" ' - TRUE
"""