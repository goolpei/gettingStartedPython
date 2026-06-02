nums = [1, 2, 3, 4, 5]

squared = [x ** 2 for x in nums]

filtered = [x for x in nums if x % 2 == 0]

sum_nums = sum(nums)



print(squared)
print(filtered)
print(f'Sum: {sum_nums}')

import os
files = os.listdir('.')
print(files)