def get_tournament_standings(string):
    l = string.split()

    s = { 'tie':1,
         'win':3,
         'loss':0
         }

    d = { 'tie':0,
         'win':0,
         'loss':0  
         }
    
    for st in l:
        if st in d:
            d[st] += 1

    for st in  d:
        if st in s:
            d[st] *= s[st]
    
    d = sorted(d.items(), key = lambda x: -x[1])

    for k in d:
        print(f"{k[0]}: {k[1]} points")
    
    

get_tournament_standings("win loss win win tie loss win")