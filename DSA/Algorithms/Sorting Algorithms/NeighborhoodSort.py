# my own sort
def neighborhood_sort(arr):
    n = len(arr) - 1
    i = 0 # sorted boundary pointer

    def check_neigbors(arr, index):
        if index == 0:
            return arr[index] <= arr[index + 1]
        elif index == n:
            return arr[index] >= arr[index - 1]
        else:
            return arr[index - 1] <= arr[index] <= arr[index + 1] 

    while i < n:

        j = i # current pointer
        
        while True:

            if j == 0:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
                else:
                    break
            elif j == n:
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
                else:
                    break
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
                elif arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
                else:
                    break

        if check_neigbors(arr, i):
            i += 1

arr = [6, 2, 3, 9, 3, 3,2,4,5,6,7,9,0,1]
neighborhood_sort(arr)
print(arr)
