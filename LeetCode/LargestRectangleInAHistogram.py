from typing import List
# TLE Solution
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         # Exploratory brute-force solution
#         max_height = max(heights)
#         n = len(heights[::])
#         def explore_neighbors(index, arr):
#             left_ptr = index - 1
#             right_ptr = index + 1
           
#             while right_ptr < n and arr[right_ptr] >= arr[index]:
#                 right_ptr += 1
#             while left_ptr > -1 and arr[left_ptr] >= arr[index]:
#                 left_ptr -= 1
            
#             width = (index - left_ptr) + (right_ptr - index) - 1
#             return arr[index] * width

#         for i in range(n):
#             h = explore_neighbors(i, heights)
#             if h > max_height:
#                 max_height = h
#         return max_height

def largestRectangleArea(heights: List[int]) -> int:
    # Exploratory brute-force solution
    max_area = 0
    heights.append(0)
    n = len(heights)
    stack = []

    for i in range(n):

        while stack and heights[i] < heights[stack[-1]]:

            h_idx = stack.pop()
            height = heights[h_idx]
            if stack:
                width = i - stack[-1] - 1
            else:  
                width = i

            area = width * height
            if area > max_area:
                max_area = area

        stack.append(i)

    return max_area