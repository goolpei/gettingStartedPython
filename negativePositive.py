nums = [1, -3, 5, -7, 0, 0, 3, 0, 2, -1]
i = 0
negative = 0
zero = 0
positive = 0

while i < len(nums):
    if nums[i] < 0:
        negative += 1
    elif nums[i] == 0:
        zero += 1
    elif nums[i] > 0:
        positive += 1

    i += 1

print("Negatives:", negative)
print("Zeroes:", zero)
print("Positives:", positive)
