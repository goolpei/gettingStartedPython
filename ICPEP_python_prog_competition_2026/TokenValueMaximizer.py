def isVowel(s):
    char = s.lower()
    return char in 'aeiou'
    
def isConsonant(s):
    char = s.lower()
    return char in 'bcdfghjklmnpqrstvwxyz'

def isInt(i):
    char = i.lower()
    return char in '1234567890'

def calc_stringval(s):
    res = s.lower()
    val_count = 0
    
    for i in range(len(res)):
        if isVowel(res[i]):
            val_count += 2
        elif isInt(res[i]):
            val_count += int(res[i])
        elif isConsonant(res[i]):
            val_count += 1 
        else:
            val_count += 0
        
    return val_count


main_string = input("Enter the main string: ")
delimiter_string = input("Enter the delimiter string: ")

for d in delimiter_string:
    main_string = main_string.replace(d, " ")

substrings = main_string.split()

val_max = -1
final_string = ""


for substring in substrings:
    if calc_stringval(substring) > val_max:
        val_max = calc_stringval(substring)
        final_string = substring

print(f"Result: {final_string}")