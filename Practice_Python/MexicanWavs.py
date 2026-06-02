def wave(string):
    if not string or string == ' ': return []
    res = []
    string = list(string)
    n = len(string)
    i = 0
    while i < n:
        string = list(string)
        if string[i] == ' ': i += 1
        else: 
            string[i] = string[i].upper()
            string = ''.join(string)
            res.append(string)
            string = string.lower()
            i += 1
            
    return res


s = 'hello'

print(wave(s))