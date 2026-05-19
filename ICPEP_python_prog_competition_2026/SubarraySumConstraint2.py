arr_len, target_sum, min_len = map(int, input("Enter N, S, and L: ").split())
arr = list(map(int, input("Enter the array elements: ").split()))
count = 0

for i in range(arr_len):
    for j in range(arr_len):
        if j - i + 1 >= min_len and sum(arr[i:j + 1]) <= target_sum:
            count += 1 
print(f"Count: {count}")
