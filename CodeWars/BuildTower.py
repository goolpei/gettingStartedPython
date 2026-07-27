def tower_builder(n_floors):
    tower = []
    rows = n_floors
    space = rows - 1
    stars = 1
    for i in range(n_floors):
        s = ''
        for _ in range(space):
            s += ' '
        for _ in range(stars):
            s += '*'
        for _ in range(space):
            s += ' '
            
        space -= 1
        stars += 2
        
        tower.append(s)
        
    return tower

print(tower_builder(5))
        
        
        