arr = []
sum = 0


while True:
    num = int(input("Enter number (Enter 0 to stop): "))
    arr.append(num)
    if num == 0: break

i = 0
while i < len(arr): 
    sum += arr[i]
    i += 1 

print("Sum:", sum)
