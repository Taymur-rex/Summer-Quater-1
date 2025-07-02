# This program will allocate team ramdomly from a list of 
# 1 Import the ramdon module 






import random

players = ("Devon", "Max", "Braylen",
           "Ollie", "Xavier", "Avery",
           "Carl", "Walter", "Darren", 
           "EJ", "Nahome", "Joaquin", 
           "Marchaun", "JaDen", "Isaiah",
           "Kenlon", "Nishad", "Kauri",
           "Kriss", "Joesph", "Semaj", 
           "Tay", "Taqari", "Jamauri",
           "Jeffery"
           )
def PickTeam(player):
    random.shuffle(players)
    team1 = player[:len (player) // 2 ]
    teamCaptia1 = team1[random.range(0,13)]  

    print("TEAM 1:")
    print("Team 1 Captain:" + teamCaptial)
    for player in team1:
         print(player)
   
    team2 = player[len (player)// 2:]
    teamCaptia2 = team2[random.range(0,12)]

    print("TEAM 2")
    print("Team 2 Captain:" + teamCaptia2)
    for player in team2:
         print(player)




PickTeam(players)    

