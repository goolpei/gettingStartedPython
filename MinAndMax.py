arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 2, 100]
min_num = arr[0]
max_num = arr[0]

for i in range(0, len(arr)):
    if arr[i] < min_num: min_num = arr[i]
    if arr[i] > max_num: max_num = arr[i]

print("Minimum:", min_num)
print("Maximum:", max_num)