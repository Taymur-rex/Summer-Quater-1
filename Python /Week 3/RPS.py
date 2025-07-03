




def RPS():
    print("Welcome to Rock Paper Scissors")
    player1 = input("Player 1 , Please enter your name")
    player2 = input("Player 2, Please enter your name")

    p1_Choice = input("{player1}, choose rock, paper, scissors ")
    while not IsValidMove(p1_Choice):
        print("Invalid Move.")
        p1_Choice = input("{player1}, choose rock, paper, scissors ")
    
    
    p2_Choice = input("{player2}, choose rock, paper, scissors ")
    while not IsValidMove(p2_Choice):
        print("Invalid Move.")
        p2_Choice = input("{player2}, choose rock, paper, scissors ")
    


    if p1_Choice == p2_Choice:
        print("It's a tie.")
    elif p1_Choice == "rock" and p2_Choice == "paper":
        print("Rocks beats scissors, {player1} wins")
    elif p1_Choice == "paper" and p2_Choice == "rock":
        print("paper beats rock, {player1} wins")
    elif p1_Choice == "scsssors" and p2_Choice == "paper":
        print("Scissors beats paper, {player1} wins")
    elif p2_Choice == "rock" and p1_Choice == "paper":
        print("Rocks beats scissors, {player2} wins")
    elif p2_Choice == "paper" and p1_Choice == "rock":
        print("paper beats rock, {player2} wins")
    elif p2_Choice == "scsssors" and p1_Choice == "paper":
        print("Scissors beats paper, {player2} wins")



def IsValidMove(PlayerMove):
    validMoves = ["rock", "paper", "scissors"]
    if PlayerMove in validMoves:
        return True
    else:
        return False
















RPS()