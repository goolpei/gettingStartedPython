line1 = input("Enter N, S, and L: ").split()
n = int(line1[0])
s_target = int(line1[1])
l_min = int(line1[2])

elements = list(map(int, input("Enter the array elements: ").split()))

count = 0

for i in range(n):
    current_sum = 0
    
    for j in range(i, n):
        current_sum += elements[j]
        
        length = j - i + 1 
        
        if length >= l_min  and current_sum <= s_target:
            count += 1 
            
        if current_sum > s_target:
            break
        
print(f"Count: {count}")