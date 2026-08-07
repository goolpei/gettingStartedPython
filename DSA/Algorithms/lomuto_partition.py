def lomuto_partition(arr, low, high):
    pivot = arr[high]
    j = 0 # scanner
    i = low - 1 # boundary

    while j < high:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]


arr = [5,4,3,2,5,1,4,3]

lomuto_partition(arr, 0, len(arr) - 1)
print(arr)