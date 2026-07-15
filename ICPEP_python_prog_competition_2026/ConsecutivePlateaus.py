def countPlateau(seq):
    
    plateau_count = 0
    
    i = 0
    j = i + 1
    
    seen = 0
    
    while(i < len(seq) and j < len(seq)):
        if seq[i] == seq[j] and seq[j] != seen:
            plateau_count += 1
            seen = seq[i]
            
        i += 1
        j += 1
        
    return plateau_count
            

sequence = list(map(int, input("Enter sequence: ").split()))

p_count = countPlateau(sequence)
print(f"Plateau count: {p_count}")