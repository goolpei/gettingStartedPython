nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

negative = 0
zero = 0
positive = 0

for num in nums:
    if num < 0:
        negative += 1
    elif num == 0:
        zero += 1
    else:
        positive += 1

print("Negatives:", negative)
print("Zeroes:", zero)
print("Positives:", positive)