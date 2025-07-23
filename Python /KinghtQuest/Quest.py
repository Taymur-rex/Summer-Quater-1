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
            square = MAP [y][x]
            if square == "w":
                screen.blit("wall", GetSrceenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetSrceenCoords(x, y))

def Draw():
    DrawBackgound()


pgzrun.go()