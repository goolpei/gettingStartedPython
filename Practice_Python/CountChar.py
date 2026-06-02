string = 'aaaabbbcccaad'

def count_char(s):
    counts = {}
    s = list(s)
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

print(count_char(string))
