n = 3

row_nums = 0
sum = 0
i = 1
j = 1
while i <= n:
    row_nums += i
    i += 1

print(row_nums)

o = 1
while(o <= row_nums):
    sum += j
    j += 2
    o += 1
    
print(sum)