# exchange_sort
def exchange_sort(arr, reverse = False):
    n = len(arr)
    i = 0
    while(i < n):
        j = i + 1
        while(j < n):
            if reverse: 
                comparison = arr[j] > arr[i]
            else:
                comparison = arr[j] < arr[i]
            if(comparison):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j += 1
        i += 1
    return arr

arr = list(map(int, input("Enter an array of numbers: ").split()))
choice = input("Ascending (Enter 'a') or Descending (Enter 'd)?: ")
if choice == 'a':
    sorted_arr = exchange_sort(arr)
else:
    sorted_arr = exchange_sort(arr, reverse=True)

print(sorted_arr)