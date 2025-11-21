str = "I love Nayeon!"
result = ""

for i in range(len(str) -1, -1, -1):
    result += str[i]

print(result)


res = ""

i = len(str) - 1
while(i >= 0):
    res += str[i]
    i -= 1

print(res)

