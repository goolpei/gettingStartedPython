from typing import List

# o(n^2) solution
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts_0 = 0
        counts_1 = 0
        for c in students:
            if c == 0: counts_0 += 1
            else: counts_1 += 1

        
        while students:
            if students[0] == sandwiches[0]:
                if students[0] == 0: counts_0 -= 1
                else: counts_1 -= 1
                students.pop(0)
                sandwiches.pop(0)
            else:
                if sandwiches[0] == 0 and counts_0 == 0: return len(students)
                if sandwiches[0] == 1 and counts_1 == 0: return len(students)
                temp = students.pop(0)
                students.append(temp)
                
        return 0

# o(n) solution
def countStudents(students: List[int], sandwiches: List[int]) -> int:
        counts_0 = 0
        counts_1 = 0
        for c in students:
            if c == 0: counts_0 += 1
            else: counts_1 += 1
        counts = [counts_0, counts_1]
        
        ptr = 0
        while ptr < len(sandwiches):
            
            sandwich = sandwiches[ptr]
            if counts[sandwich] == 0:
                break
            counts[sandwich] -= 1
            ptr += 1
        
        return counts[0] + counts[1]

st = [1,1,0,0]
sw = [0,1,0,1]
print(countStudents(st, sw))