from collections import defaultdict

l = defaultdict(list)
l[1].append(2)
l[0].append('a')
l[1].append(1)
l[1] = [3]

print(l)