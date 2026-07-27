class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = [] # contains list of transactions

    def __str__(self):
        string_output = ''
        for item in self.ledger:
            string_output += f"{item['description']:<23.23}{item['amount']:>7.2f}\n" 
        string_output += f'Total: {self.get_balance():.2f}'
        return f'{self.name:*^30}\n' + string_output
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        # return true if withdrawing succeeded else false
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': 
            description})
            return True
        return False

    def get_balance(self):
        # self.ledger = [{a:a, d:d},{a:a, d:d}]
        return sum([x['amount'] for x in self.ledger])

    def transfer(self, amount, other):
        # return true if transferring succeeded else false
        if self.check_funds(amount):
            self.withdraw(amount, description = f'Transfer to {other.name}')
            other.deposit(amount, description = f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return False if amount > self.get_balance() else True

    def total_withdrawn(self):
        return sum([x['amount'] for x in self.ledger if x['amount'] < 0 and 'Transfer' not in x['description']]) * -1

# chop off the decimal
def school_round_ten(x):
    return int((x + 5) // 10) * 10

def create_spend_chart(categories):
    total_withdrawals = 0
    list_category_spent = {category.name:category.total_withdrawn() for category in categories}
    for category in list_category_spent:
        total_withdrawals += list_category_spent[category]
    
    percentage_per_category = {c.name:c.total_withdrawn() * 100 // total_withdrawals for c in categories}
    graph =  "Percentage spent by category"
    graph += '\n'
    for i in range(10, -1, -1):
        graph += f'{str(i*10):>3}|'

        for c in percentage_per_category:
            if percentage_per_category[c] >= i * 10: # didn't use the school_round_ten function, the problemset didn't consider the roundings correct
                graph += ' o ' 
            else:
                graph += '   '

        graph += ' \n'
    graph += ' '*4 + '---'*len(categories) + '-\n'
    
    len_category = [len(x.name) for x in categories]
    
    for i in range(max(len_category)):
        graph += ' ' * 4
        for c in categories:
            graph +=' ' 
            if len(c.name) > i:
                graph += c.name[i]
            else:
                graph += ' '
            graph +=' '
        graph += ' \n'
    return graph.strip('\n')

    
def main():
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(150.89, 'restaurant and more food for dessert')
    
    clothing = Category('Clothing')
    clothing.deposit(1000)
    clothing.withdraw(550)
    
    auto = Category('Auto')
    auto.deposit(1000)
    auto.withdraw(660)

    categories = [food, clothing, auto]
    
    print(create_spend_chart(categories))
    
if __name__ == '__main__':
    main()