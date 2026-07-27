from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in seen: return [i, seen[find]]
            seen[nums[i]] = i
        return []
              