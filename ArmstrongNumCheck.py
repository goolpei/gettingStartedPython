# a^3 + b^3 + c^3 = abc

def isArmstrongNum(n):
    
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    if(a**3 + b**3 + c**3 != n):
        return False
    
    return True


num = int(input("Enter a 3 digit number: "))

if(isArmstrongNum(num)):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


