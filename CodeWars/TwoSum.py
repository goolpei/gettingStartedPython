def get_two_sum(arr, target):

    left = 0
    while left < len(arr):

        a = target - arr[left]
        if a in arr:
            return [arr[left], a]
        left += 1

  
arr = [1, 2, 3, 4, 5]

print(get_two_sum(arr, 6))