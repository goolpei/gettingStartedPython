
arrNum = list(map(int, input().split()))
arrNum2 = arrNum.copy()
arrNum3 = arrNum[:]


n = len(arrNum)

for i in range(n):
    for j in range(i + 1, n):
        if arrNum[i] > arrNum[j]:
            arrNum[j], arrNum[i] = arrNum[i], arrNum[j]



print(arrNum)
print(arrNum2)
print(sorted(arrNum2))

print(arrNum3)
arrNum3.sort()
print(arrNum3)