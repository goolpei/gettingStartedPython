# pick/selection sort

# selection sort is a blind type of sort, it cannot be optimized.
# always runs at O(n*2)
def selection_sort(arr):
    i = 0
    while i < len(arr):
        min_index = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1

        arr[i], arr[min_index] = arr[min_index], arr[i]
        i += 1
    return arr

arr = [4,3 ,2, 32,3,2,5,6,67]

print(selection_sort(arr))