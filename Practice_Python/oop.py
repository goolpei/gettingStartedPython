class Transaction():
    def __init__(self, what, how_much, when):
        self.what = what
        self.how_much = how_much
        self.when = when

    def show_details(self):
        print(f"Expense name: {self.what}")
        print(f"Expense cost: {self.how_much}")
        print(f"Time of expense: {self.when}")
        

t1 = Transaction("Food", 100, '12PM')
 
t1.show_details()