arr = [2, 3, 8, 7, 5]
n = 5
min_val = arr[0]

for i in range(n):
    if(arr[i] < min_val):
        min_val = arr[i]

print("Minimum value:", min_val)