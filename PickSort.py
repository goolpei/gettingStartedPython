nums = []
print("Enter 5 numbers:", end=" ")
for i in range(0, 5):
    nums.append(int(input()))

print("Ascending (Enter 'a') or Descending (Enter 'd)?:", end=" ")
choice = input()
if choice == 'a':
    i = 0
    while(i < 5):
        j = i + 1
        while(j < 5):
            if(nums[j] < nums[i]):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

            j += 1
        i += 1
else:
    i = 0
    while(i < 5):
            j = i + 1
            while(j < 5):
                if(nums[j] > nums[i]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

                j += 1
            i += 1

print(nums)