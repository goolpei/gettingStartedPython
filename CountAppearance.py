arr = [1, 5, 5, 5, 2, 2, 5, 5, 2, 3]
i = 0
count_five = 0
while i < 10:
    if arr[i] == 5: count_five += 1
    i += 1
print("Number of fives:", count_five)