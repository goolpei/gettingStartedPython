from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        comp = [x for x in range(1, len(nums) + 1)]
        lost = 0
        double = 0
        for num in comp:
            if num not in nums: 
                lost = num
                break

        for num in nums:
            if nums.count(num) > 1: double = num
            if lost and double: break
        
        return [double, lost]

print(findErrorNums([1,2,2,4]))