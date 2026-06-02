#vowel shifter
vowels = ['a', 'e', 'i', 'o', 'u', 'a']
vowelsU = ['A', 'E', 'I', 'O', 'U', 'A']

s = list(input("Enter string: "))

for i, c in enumerate(s):
    if c in vowels:
        s[i] = vowels[vowels.index(c) + 1]
    elif c in vowelsU:
        s[i] = vowelsU[vowelsU.index(c) + 1]

print(''.join(s))