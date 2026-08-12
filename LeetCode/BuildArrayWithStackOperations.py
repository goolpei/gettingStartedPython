from typing import List
# mine
def buildArray(target: List[int], n: int) -> List[str]:
        
        if n < 1: return []

        stack = []
        operations = []
        stream = [i for i in range(n, 0, -1)]

        i = 0
        while stream and stack != target:

            stack.append(stream.pop())
            operations.append('Push')

            while stream and stack[i] != target[i]:
                stack.pop()
                operations.append('Pop')

                stack.append(stream.pop())
                operations.append('Push')

            i += 1
        
        return operations if stack == target else []

print(buildArray([1,3], 3))


# gemini

# class Solution:
#     def buildArray(self, target: List[int], n: int) -> List[str]:
#         operations = []
#         target_idx = 0
        
#         # We iterate from number 1 up to n
#         for num in range(1, n + 1):
#             # If we've already matched all numbers in target, we're done!
#             if target_idx == len(target):
#                 break
                
#             operations.append("Push")
            
#             # If the current stream number matches target's expected number
#             if num == target[target_idx]:
#                 target_idx += 1  # Move to the next number we need to match
#             else:
#                 # If it doesn't match, pop it immediately
#                 operations.append("Pop")
                
#         return operations