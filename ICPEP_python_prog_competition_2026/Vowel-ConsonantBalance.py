def isVowel(s):
    char = s.lower()
    return char in 'aeiou'
    
s = input("Enter string: ")
n = len(s)
max_length = 0

for i in range(n):
    
    vowels = 0
    consonants = 0
    
    for j in range(i, n):
        if isVowel(s[j]):
            vowels += 1
        else:
            consonants += 1
            
        if vowels == consonants:
            current_length = j - i + 1
            if current_length > max_length:
                max_length = current_length

print(f"Result: {max_length}")