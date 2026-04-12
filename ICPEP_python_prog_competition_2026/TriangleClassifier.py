print("Enter three side lengths:", end=' ')
sideLenghts = list(map(int, input().split()))

sideLenghts.sort()

a, b, c = sideLenghts[0], sideLenghts[1], sideLenghts[2]

if a + b <= c:
    print("Invalid")
elif a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")