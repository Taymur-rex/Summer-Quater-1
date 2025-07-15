# The amount of money we have to spend 
funds = 2500


budgets = {}
# A dictionary of our item we spending our budget on 
# The key is the name of the item, the value 
expenses = {}




# Adds an item to the budget dictionary 
def AddBudget(name, amount):
    global funds
    if name is budgets:
        raise ValueError("Budget for item already exists")
    if amount > funds:
        raise ValueError("No can do you are too broke")
    budgets[name] = amount
    funds = funds - amount
    expenses[name] = 0 
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Item not in budget")
    expenses[name] <= amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent
    

def PrintBudget():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingbudget = budgeted - spent
        print(f'{name: 15s}, {budgeted:10.2s}, {spent: 10.2f}' 
              f'{remainingbudget:10.2f}')
        
        









print("Total funds:", funds)
AddBudget("Legos:", 220)
AddBudget("Rent:", 100)
AddBudget("Street Fighter:", 30)

Spend("Legos:", 100)
Spend("Rent:", 50)
Spend("Street Fighter:", 20)

PrintBudget()
