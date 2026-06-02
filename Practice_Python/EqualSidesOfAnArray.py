
def get_sum_between_points(arr, a, b):
    if a > b: return 0
    sum = 0
    for i in range(a, b + 1):
        sum += arr[i]
    return sum
    

def find_even_index(arr):
    pointer = 0
    while pointer < len(arr):

        left_sum = get_sum_between_points(arr, 0, pointer - 1)
        right_sum = get_sum_between_points(arr, pointer + 1, len(arr) - 1)

        if left_sum == right_sum: return pointer
        pointer += 1
    return -1

def find_even_index2(arr): # codewars top answer
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


print(find_even_index([1,2,3,4,3,2,1]))