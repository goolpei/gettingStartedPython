from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    middle = [x for x in arr if x == pivot]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle +  quick_sort(right)


arr = [1,4,2,3,4,5]
arr2 = [2, 3, 5, 1, 6, 8,4, 3,2, 1,2]
k = arr + arr2
print(k)
print(quick_sort(k))
    