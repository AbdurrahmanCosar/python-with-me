# age >= 18 ve (mezuniyet == "lise" ya da mezuniyet == "üniversite")


# And Operatörü (ve)
x = 10
#result = 5 < x < 15
result = ( x > 5 ) and (x < 15) 
# True ve True => True
# False ve True => False
# False ve False => False
print(result)

# or operatörü (veya)

resultOr = (x > 0 ) or (x % 2 == 0) 
# True ve False => True
# True veya True => True
# False ve False => False
print(resultOr)

# not operatörü 
resultNot = not(x > 0 )
print(resultNot)


# x, 5-10 arasında bir çift sayı mı? 

print ((x > 5) and (x < 10) and (x%2 == 0))
