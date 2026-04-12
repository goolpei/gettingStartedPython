line1 = input("Enter window size and tolerance: ").split()
W = int(line1[0])
T = int(line1[1])

stream_input = input("Enter data stream (end with -1): ").split()
data = [int(x) for x in stream_input[:-1]]

valid_count = 0

n = len(data)

for i in range(n - W + 1):
    current_window = data[i : i + W]
    
    diff = max(current_window) - min(current_window)
    
    if diff <= T:
        valid_count += 1 
        
print(f"Valid Windows: {valid_count}")