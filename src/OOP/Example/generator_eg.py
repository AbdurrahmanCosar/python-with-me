# (1'den sonsuza kadar) her sayının karesini getiren bir fonksiyon
# Fibonacci serisini hem normal hem de generator fonksiyon ile oluşturun
# Performans testlerini yapın

# 1 
def kare_al():

    num = 1

    while True:
        yield num**2
        num += 1


# 2
def fibonacci_normal(max):

    sayilar = []

    a, b = 0,1

    while len(sayilar) <= max:
        
        sayilar.append(b)
        a, b = b, a + b
    return sayilar


def fibonacci_generator(max):

    num = 1
   
    a, b = 0, 1

    while num <= max:
        
        a, b = b, a+b
        yield a
        num += 1


# 3

# KAPLADIĞI ALAN
import sys

list_ = [i*2 for i in range(10000)]
print(sys.getsizeof(list_)) # Bellekte Kapladığı Alan

gen_ = (i*2 for i in range(10000))
print(sys.getsizeof(gen_)) # Bellekte kapladığı alan

# HIZ

import time

gen_start_time = time.time()
sum((i**2 for i in range(10000)))
gen_stop_time = time.time() - gen_start_time


list_start_time = time.time()
sum([i**2 for i in range(10000)])
list_stop_time = time.time() - list_start_time
print(gen_stop_time)
print(list_stop_time)