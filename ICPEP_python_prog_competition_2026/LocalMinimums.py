arr = list(map(int, input("Enter elements: ").split()))

n = len(arr)
mins = []

if n == 1:
    mins.append(arr[0])
else:
    for i in range(n):
        if i == 0:
            if arr[i] <= arr[i + 1]: mins.append(arr[i])
        elif i == n - 1:
            if arr[i] <= arr[i - 1]: mins.append(arr[i])
        else:
            if arr[i-1] >= arr[i] <= arr[i + 1]: mins.append(arr[i])
print(mins)