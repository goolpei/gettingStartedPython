arr = []
invalid = 0; cold = 0; warm = 0; hot = 0;

print("Enter 10 temperatures:", end=" ")
for i  in range(10):
    num = int(input())
    arr.append(num)

for i in range(10):
    if arr[i] < 0 or arr[i] > 100: invalid+=1
    elif arr[i] < 20: cold+=1
    elif arr[i] >= 20 and arr[i] <= 30: warm+=1
    else: hot+=1

print("Number of cold temperatures:", cold)
print("Number of warm temperatures:", warm)
print("Number of hot temperatures:", hot)
print("Number of invalid temperatures:", invalid)