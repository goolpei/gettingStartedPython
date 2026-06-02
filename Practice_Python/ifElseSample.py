a = -10
b = -10

print ("-----------------------------")
if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both are equal")
print ("-----------------------------")

#s=salary
s = 25000

if s < 25000:
    tax = 0
elif s >= 25000:
    tax = s * (6 / 100)
else:
    tax = s * (12 / 100)

print (tax)
print ("-----------------------------")

#hr=hour

hr = 7

if hr <= 3:
    fee = 50 * hr
elif hr > 3 and hr <= 6:
    fee = 35 * hr
elif hr > 6 and hr <= 12:
    fee = 20 * hr
else:
    fee = 10 * hr

print ("Fee:", fee, "Pesos")
print ("-----------------------------")



