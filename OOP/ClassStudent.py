class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def showStudentDetails(self):
        if self.grade < 0 and self.grade > 100:
            print(f'{self.name} has invalid grade.')
        elif self.grade < 75:
            print(f'{self.name} failed')
        else:
            print(f'{self.name} passed')
        
s1 = Student('Mat', 100)
s1.showStudentDetails()