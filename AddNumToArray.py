arr = []
while(True):
    print("Enter number to add to array (enter 'x' to exit):", end=" ")
    try:
        num = int(input())
    except ValueError:
        break 

    arr.append(num)

    
    print("Array contents:",arr)

print("Program terminated.")

