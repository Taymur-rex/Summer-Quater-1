# 1. Create a list of items in your room you can potentially pack.
# 2. Create an empty list to represent your travel bag 
# 3. Repeatedly prompt the user for the index of an item to put in their travel bag by removing it from the the list of items in your room to your travel bag list.
# 4. Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this.
# 5. Print the contents of your luggage for the trip, as well as the number of items you decided to bring
Room = ["Clothes", "Wallet", "Keys", "Gaming Laptop", "Etc", "Headphones "]

Travelbag = []


print("Pack your back")
print("Enter the inbox an item you'd like to from your room in your bag")
print("Type 'molly' whenyour done packing./n")
print("your bedroom")


for item in Room:
    print(item)


item = int(input("Item Inbox: "))


while item != 100:
    Travelbag.append(Room[item])
    Room.remove(Room[item])
    print("\n Your Bedroom:")
    print(Room)
    print("\n Your Travel Bag:")
    print(Travelbag)
