geniuse =["Kamari", "Kris", "Joaquin", "Jeffery", "Tay"]

for genius in geniuse:
    print(genius)


answer = input("Would you like me to print this list again Y/N?")
while answer == "Y":
    for genius in geniuse:
        print(genius)
    answer = input("Would you like me to print this list again Y/N?")