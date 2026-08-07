def insertion_sort(arr):
    n = len(arr)

    sorted_count = 1
    
    while sorted_count < n:
        j = sorted_count
        while j > 0:

            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
            j -= 1

        sorted_count += 1

arr = [3,4,5,2,1]
insertion_sort(arr)
print(arr)