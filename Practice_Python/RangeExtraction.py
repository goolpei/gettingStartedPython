def solution(args):
    result = []
    i = 0
    
    while i < len(args):
        # Start of a potential range
        start = args[i]
        j = i
        
        # Look ahead to find the end of the consecutive sequence
        while j + 1 < len(args) and args[j + 1] == args[j] + 1:
            j += 1
            
        # Check if the sequence is at least 3 numbers long
        if j - i >= 2:
            # Format as a range: "start-end"
            result.append(f"{start}-{args[j]}")
            # Move the pointer to the next number after the range
            i = j + 1
        else:
            # Not a range of 3+, just add the single number
            result.append(str(start))
            i += 1
            
    return ",".join(result)