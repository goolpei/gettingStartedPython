def reverseNum(n):
    rev = 0
    while(n != 0):
        rev = rev * 10 + (n % 10)
        n = n // 10
    
    return rev

num = int(input("Enter number: "))

print(f"Reversed Number: {reverseNum(num)}")