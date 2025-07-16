class Budget():
    def __init__(self):
        self.funds = 2500
        self.budgets = {}
        self.expenses = {}





def AddBudget(name, amount):
    global self.funds
    if name is self.budgets:
        raise ValueError("Budget for item already exists")
    if amount > self.funds:
        raise ValueError("No can do you are too broke")
    self.budgets[name] = amount
    self.funds = self.funds - amount
    self.expenses[name] = 0 
    return self.funds

def Spend(name, amount):
    if name not in self.expenses:
        raise ValueError("Item not in budget")
    self.expenses[name] += amount
    budgeted = self.budgets[name]
    spent = self.expenses[name]
    return budgeted - spent
    

def PrintBudget():
    print("Budget              Budgeted      Spent    Remaining ")
    print("--------------------------------------------------------------------")
    totalBudget = 0
    totalSpent = 0
    totalRemaining = 0 
    for name in self.budgets:
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        remainingbudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}' 
              f'{remainingbudget:10.2f}')
        
    totalBudget += budgeted
    totalSpent += spent
    totalRemaining += remainingbudget
    print(f'{"Total":15s}, {totalBudget:10.2f}, {totalSpent:10.2f}' 
              f'{remainingbudget:10.2f}')






print("Total self.funds:", self.funds)
AddBudget("Legos:", 220)
AddBudget("Rent:", 100)
AddBudget("Street Fighter:", 30)

Spend("Legos:", 100)
Spend("Rent:", 50)
Spend("Street Fighter:", 20)

PrintBudget()
