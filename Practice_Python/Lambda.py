students = [("Alice", 20, 90), ("Bob", 19, 95), ('Carl', 15, 80)]

sorted_students = sorted(students, key = lambda x: x[-1])

print(sorted_students)