def count_diff(plank1, plank2):
    count = 0
    for i, j in zip(plank1, plank2):
        if i != j: count += 1
    return count
        

def ship_of_theseus(ship):
    if len(ship) == 1 or not ship: return True
    store_ones = []
    
    i = 0
    j = i + 1
    while True:
        if i == len(ship) - 1: break
        if len(ship[i]) != len(ship[j]): return False
        store_ones.append(count_diff(ship[i], ship[j]))
        i += 1
        j += 1
        
    return True if sum(store_ones)/(len(ship) - 1) == 1 else False
        