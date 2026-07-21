class Class:
    def __init__(self, att) -> None:
        self.att = att
    

c = Class(5)
print(c.att)
c.att = 6
print(c.att)