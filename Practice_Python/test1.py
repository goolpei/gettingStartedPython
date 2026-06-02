arr = [5, 2, 9, 1, 0]
min_val = arr[0]
for num in arr[1:]:
    if num < min_val:
        min_val = num
print("Minimum value:", min_val)