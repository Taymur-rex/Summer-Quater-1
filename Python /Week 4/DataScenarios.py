#1. A restaurant menu with prices for each item
#2. High scores to an arcade game
#3. All of the months of the year
#4. All the items in your backpack
#5. Look up Student emails by their names
#6. A shopping cart of groceries 
#7. [Add a scenario of your own]


print("Scenarios #1: A restaurant menu with prices for each item")
print("Best Structure: Dixtonary: best to pair food with pasta in keyvalue")
menu ={
    "French Toast": 12,
    "Grand slam": 12,
    "T-bone Steak": 10,
    "Avacado Toast": 15
}
for key, item in menu.items():
    print(key ":", item)

print("Scenarios #2: High scores to an arcade game")
print("Best Structure: List: Need a mutable strutucre tto be able to change in real time")
highScores ={
    100,
    105,
    110,
    99
}

print("Scenarios #3: All of the months of the year ")
print("Best Structure: Tuple: the month do not change")
