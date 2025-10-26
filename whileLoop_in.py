numbers = []
i = 0

print("Enter five numbers:")
while i < 5:
    num = int(input())
    numbers.append(num)
    i += 1

print("You entered:", end=" ")
i = 0
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1