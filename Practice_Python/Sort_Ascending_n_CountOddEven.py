arr = []
count_odd = 0
count_even = 0
print("Enter 7 numbers: ")
for i in range(0, 7):
    nums = int(input())
    arr.append(nums)

#sort
i = 0
j = 0
for i in range(0, 7):
    j = i + 1
    for j in range(0, 7):
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

        j += 1
    
    i += 1

print(arr)
i = 0
for i in range(0, 7):
    if arr[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Amount of even numbers:", count_even)
print("Amount of odd numbers:", count_odd)
