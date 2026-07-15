# from gemini 
from itertools import zip_longest

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = "\n".join(f"{item['description']:<23.23}{item['amount']:>7.2f}" for item in self.ledger)
        total = f'\nTotal: {self.get_balance():.2f}'
        return title + items + total
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(x['amount'] for x in self.ledger)

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, description=f'Transfer to {other.name}')
            other.deposit(amount, description=f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def total_withdrawn(self):
        # Exclude negative amounts that represent transfers out
        return sum(
            abs(x['amount']) 
            for x in self.ledger 
            if x['amount'] < 0 and not x['description'].startswith("Transfer to")
        )


def create_spend_chart(categories):
    # 1. Calculate total spent across all categories
    total_spent = sum(c.total_withdrawn() for c in categories)
    if total_spent == 0:
        total_spent = 1  # Prevent ZeroDivisionError
    
    # 2. Get percentages rounded down to nearest 10
    percentages = {c.name: int((c.total_withdrawn() / total_spent) * 10) * 10 for c in categories}
    
    # 3. Build the bar graph
    lines = ["Percentage spent by category"]
    for i in range(100, -1, -10):
        row = f"{i:>3}|"
        for c in categories:
            row += " o " if percentages[c.name] >= i else "   "
        lines.append(row + " ") # Add the trailing space required by fCC tests
        
    # 4. Add the horizontal line separator
    lines.append("    " + "-" * (len(categories) * 3 + 1))
    
    # 5. Vertical category names
    names = [c.name for c in categories]
    for chars in zip_longest(*names, fillvalue=' '):
        lines.append("     " + "  ".join(chars) + "  ")
        
    return "\n".join(lines)