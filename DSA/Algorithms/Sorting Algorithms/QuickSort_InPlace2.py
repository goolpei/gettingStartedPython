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

def quick_sort(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        boundary_idx = hoare_partition(arr, low, high) # j
        quick_sort(arr, low, boundary_idx)
        quick_sort(arr, boundary_idx + 1, high)

arr = [5,4,3,2,5,1,4,1, 32, 32,1, 2,3,4]
quick_sort(arr)
print(arr)