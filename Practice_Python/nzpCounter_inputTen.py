nums = []
negative = 0
zero = 0
positive = 0

print("Enter ten numbers: ", end="")
for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    nums.append(num)

for i in range(10): 
    if nums[i] < 0: negative += 1
    elif nums[i] == 0: zero += 1
    else: positive += 1

print("Negatives:", negative)
print("Zeroes:", zero)
print("Postives:", positive)