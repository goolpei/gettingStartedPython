# gemini
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    # BASE CASE: A list with 0 or 1 element is already sorted!
    if len(arr) <= 1:
        return arr

    # 1. DIVIDE: Find the midpoint and split the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. CONQUER: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # 3. COMBINE: Merge the two sorted halves back together
    return merge(sorted_left, sorted_right)


def merge(left: List[int], right: List[int]) -> List[int]:
    sorted_result: List[int] = []
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_result.append(left[i])
            i += 1
        else:
            sorted_result.append(right[j])
            j += 1

    # Append any leftover elements from the left or right lists
    sorted_result.extend(left[i:])
    sorted_result.extend(right[j:])

    return sorted_result


# --- Example Usage ---
if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted:", numbers)
    
    sorted_numbers = merge_sort(numbers)
    print("Sorted:  ", sorted_numbers)