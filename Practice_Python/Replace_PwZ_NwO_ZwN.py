arr = [1, 3, 0, -1, 2, 9, 3, 0, 0, -1]
zeroes = 0; ones = 0; negative_ones = 0; count = 0

print("\nArray contents:", arr)

for j in range(len(arr)):
    if arr[j] > 0: 
        arr[j] = 0
        zeroes+=1
    elif arr[j] < 0: 
        arr[j] = 1
        ones+=1
    else: 
        arr[j] = -1
        negative_ones+=1

count = ones + zeroes + negative_ones

print("Replaced array:", arr) 
print("Amount of changed numbers:", count)