print("Enter array size and target sum:", end=" ")
arrSize_targetSum = list(map(int, input().split()))

arrSize = arrSize_targetSum[0] 
targetSum = arrSize_targetSum[1] 

print("Enter array elements:", end=" ")
arr_elements = list(map(int, input().split()))


index_compare = float('inf')
found = True

for j in range(arrSize):
    
    sum_compare = 0
    index_count = 0
    
    for i in range(j, arrSize):
        sum_compare += arr_elements[i]
        index_count += 1
        
        if sum_compare >= targetSum:
            if index_count < index_compare:
                index_compare = index_count
            break
        
if(index_compare == float('inf')): found = False

if(found):
    print(f"Minimal length: {index_compare}")
else:
    print(f"Minimal length: 0")