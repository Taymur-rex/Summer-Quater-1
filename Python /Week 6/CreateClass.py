
    def __init__(self, movieList, gameList,):
        self.movieList = []
        self.gameList = []
        self.favGame = ""
        self.favMovie = ""
        self.movieList = movieList
        self.gameList = gameList
    def AddGame(self, game):
        if game in self.gameList:
            print("Game is already in list")
        else:
            self.gameList.append(game)
    def AddMovie(self, movie):
        if movie in self.movieList:
            print("Game is already in list")
        else:
            self.movieList.append(movie)
    def RemoveGame(self, game):
        if game in self.gameList:
            self.gameList.remove(game)
        else:
            print("Game Not Found")
    def RemoveMovie(self, movie):
        if movie in self.movieList:
            self.gameList.remove(movie)
        else:
            print("Movie Not Found")
    def DisplayGames(self):class Collection:
        for game in self.gameList:
            print(game)
    def DisplayMovie(self):
        for movie in self.movieList:
            print(movie)
    def DisplayFavGame(self):
        print(f'Fav Game: {self.favGame}')
    def DisplayFavMovie(self):
        print(f'Fav Movie: {self.favMovie}')
    def DisplayCollection(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovie()
        self.DisplayFavMovie()
    def setfavmovie(self, movie):
        if movie not in self.movieList:
            self.AddMovie(movie)
        self.favMovie = movie
    def setfavgame(self, game):
        if game not in self.gameList:
            self.AddGame(game)
        self.favGame = game










        
        
