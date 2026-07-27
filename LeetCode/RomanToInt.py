
def romanToInt(s: str) -> int:
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    i = len(s) - 1 
    res = 0
    while True:
        right = val[s[i]] 
        if i == 0: 
            res += right
            break
        left = val[s[i-1]] 
        if right > left:
            res += right - left
            i -= 1
        else:
            res += right
        if i == 0: break
        i -= 1 
    return res

s = "MIV"
print(romanToInt(s))

class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        prev_value = 0
        
        # Traverse from right to left
        for char in reversed(s):
            current_value = val[char]
            
            # If the current value is less than the value to its right, subtract it
            if current_value < prev_value:
                res -= current_value
            # Otherwise, add it
            else:  
                res += current_value
                
            # Update prev_value for the next iteration
            prev_value = current_value
            
        return res