s = input("Enter string: ")
s = list(s)
vowels = "AEIOU"
count_v = 0
count_c = 0
res = 0
for char in s:
    if char in vowels:
        count_v += 1
    else:
        count_c += 1
if count_v == 0 or count_c == 0: res = 0
else:
    
    left = 0
    right = len(s) - 1
    while left < right:
        if count_c == count_v: 
            res = count_c + count_v
            break
        elif count_v > count_c:
            if s[left] in vowels:
                left += 1
                count_v -= 1
            elif s[right] in vowels:
                right -= 1
                count_v -= 1
        else:
            if s[left] not in vowels:
                left += 1
                count_c -= 1
            elif s[right] not in vowels:
                right += 1
                count_c -= 1
            
print(f"Result: {res}")

