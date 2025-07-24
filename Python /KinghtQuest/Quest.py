import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE




MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W  KG       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]







def GetSrceenCoords(x, y):
    return(x * GRID_SIZE, y * GRID_SIZE )


def DrawBackgound():
    for y in range (GRID_HEIGHT):
        for x in range (GRID_WIDTH):
            screen.blit("foor1", GetSrceenCoords(x, y))





def SetupGame():
    global player 
    player = pgzrun.Actor("player", anchor=("left", "top"))










def DrawScenery():
    for y in range (GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP [y] [x]
            if square == "W":
                srceen.blit("wall",GetSrceenCoords(x, y))
            elif square == "D":
                srceen.blit("wall",GetSrceenCoords(x, y))





def draw():
    srceen.clear()
    DrawBackgound()
    DrawScenery()


pgzrun.go()