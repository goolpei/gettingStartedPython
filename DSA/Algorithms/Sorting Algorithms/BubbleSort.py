def bubble_sort(arr):

    n = len(arr)

    sorted_count = 0
    while sorted_count < n:
        swapped = False
        j = 0
        while j < n - sorted_count - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            j += 1

        if not swapped:
            break
        sorted_count += 1


arr = [6, 3,4,2,5,1]
bubble_sort(arr)
print(arr)           
            
