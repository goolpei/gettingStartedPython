numbers = []
print("Enter five numbers:")
for i in range(5):
    num = int(input())
    numbers.append(num)

print("You entered:", end=" ")
for n in numbers:
    print(n, end=" ")