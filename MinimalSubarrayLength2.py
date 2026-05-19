arr_size, trgt_sum = map(int, input("Enter array size and target sum: ").split())
arr = list(map(int, input("Enter array elements: ").split()))
temp_sum = 0
min_len = arr_size
if sum(arr) < trgt_sum:
    min_len = 0
else:
    i = 0
    j = 0
    while i <= arr_size:
        if temp_sum < trgt_sum:
            i += 1
            temp_sum = sum(arr[j:i])
        else: # temp_sum >= trgt_sum
            j += 1
            temp_len = i - j + 1
            if temp_len < min_len: min_len = temp_len
            temp_sum = sum(arr[j:i])
            
print(f"Minimal length: {min_len}")
            