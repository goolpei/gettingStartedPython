def mix(s1, s2):
    letter_map_s1 = {chr(n) : 0 for n in range(97, 123)}
    letter_map_s2 = {chr(n) : 0 for n in range(97, 123)}
    
    for c in s1:
        if c.islower():
            letter_map_s1[c] += 1
    for c in s2:
        if c.islower():
            letter_map_s2[c] += 1
    res = {}
    
    for n in range(97, 123):
        if letter_map_s1[chr(n)] > 1 or letter_map_s2[chr(n)] > 1:
            if letter_map_s1[chr(n)] > letter_map_s2[chr(n)]:
                res['1:' + chr(n) * letter_map_s1[chr(n)]] = letter_map_s1[chr(n)]
            elif letter_map_s1[chr(n)] < letter_map_s2[chr(n)]:
                res['2:' + chr(n) * letter_map_s2[chr(n)]] = letter_map_s2[chr(n)]
            else:
                res['=:' + chr(n) * letter_map_s2[chr(n)]] = letter_map_s2[chr(n)]
                
    sorted_res = dict(sorted(res.items(), key = lambda x: (-x[1], x[0])))
    res_list = [x for x in sorted_res]
    return '/'.join(res_list)

print(mix('Matthew', 'Venice'))
    
                