def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while pivot > arr[i]:
            i += 1
        j -= 1
        while pivot < arr[j]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j



arr = [5, 3, 8, 4, 2, 7]

k = hoare_partition(arr, 0, len(arr) - 1)
print(arr)
print(k)