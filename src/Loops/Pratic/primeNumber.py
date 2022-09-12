#* Prime Number

number = int(input("Number: "))

isPrime = True


if number == 1:
    isPrime = False


for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break


if isPrime:
    print(" Number is Prime")

else:
    print("Number is not prime")