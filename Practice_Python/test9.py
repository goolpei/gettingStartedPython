def findClosestNumber(nums):
        mini = float('inf')
        for num in nums:
            if abs(num) <= abs(mini):
                if abs(num) == mini:
                    mini = abs(num)
                else:
                    mini = num
        return mini

nums =[-100000,-100000]
print(findClosestNumber(nums))