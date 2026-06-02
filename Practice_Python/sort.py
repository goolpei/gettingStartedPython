nums = [20, 40, 30, 50, 10]

i = 0
while i < len(nums):
    j = i + 1
    while j < len(nums):
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

        j += 1
    i += 1

print("Sorted (ascending):", nums)