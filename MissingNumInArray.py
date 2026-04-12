# Problem: You are given N integers from 1 to N + 1, but one number is missing. 
# Write a program to find that missing number

arr = []
arrComp = []

arrSize = int(input("Enter number of elements: "))

print("Enter array elements:")
for i in range(arrSize - 1):
    num = int(input())
    arr.append(num)
    arrComp.append(i + 1)

arr.append(0)
arrComp.append(i + 2)

for k in range(arrSize):
    if (arr[k] != arrComp[k]):
        missingNum = arrComp[k]
        break

print(f"Missing number: {missingNum}")

