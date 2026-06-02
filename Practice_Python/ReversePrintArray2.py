arr = [1, 2, 3, 4, 5]
result = []

for i in range(len(arr) - 1, -1, -1):
    result.append(arr[i])

print(result)