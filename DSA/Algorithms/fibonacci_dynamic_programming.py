def fibonacci(n):
    sequence = [0, 1]

    for i in range(2, n + 1):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence[n]