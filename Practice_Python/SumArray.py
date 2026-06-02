sum = 0
arr = []
print("Enter 5 numbers:", end=" ")
for i in range(5):
    num = int(input())
    arr.append(num)
    sum = sum + arr[i]

print("Sum:", sum)