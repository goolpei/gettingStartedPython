def lomuto_partition(arr, low, high) -> int:
    pivot = arr[high]
    j = low # scanner
    i = low - 1 # boundary

    while j < high:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def quick_sort(arr, low = 0, high = None) -> None: 
    # must not return anything since sorting is in-place
    # can return but would be redundant since python lists are mutable, 
    # passing them to functions doens't create a copy,
    # it passes the memory address of the list, sorting the original list

    if high == None:
        high = len(arr) - 1
    # BASE CASE: Stop when boundary is 0 or 1 element
    if low < high:

        pivot_index = lomuto_partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

arr = [5,4,3,2,5,1,4,3]
quick_sort(arr)
print(arr)

    