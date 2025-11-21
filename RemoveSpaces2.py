str = "I love N a y e o n !"
result = ""

for i in range(0, len(str) - 1):
    if str[i] != ' ':
        result += str[i]

print(result)

i = 0
res = ""

while(i < len(str) - 1):
    if str[i] != ' ':
        res += str[i]
    i += 1

print(res)