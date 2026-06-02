a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

c = list(map(lambda pair: pair[0] + pair[1], zip(a, b)))

print(c)