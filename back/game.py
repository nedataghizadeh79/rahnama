class Gameboard:
    COLUMNS = ["name", "lastname", "city", "color", "animal", "food"]

    def init(self):
        self.columns = {
            "name": "",
            "lastname": "",
            "city": "",
            "color": "",
            "animal": "",
            "food": ""
        }


class Player:
    def init(self, id):
        self.id = id
        self.gameboards = []
        self.score = 0

    def writeColumn(self, column, word):
        self.gameboards[-1].columns[column] = word


class Game:
    def init(self):
        self.players = {}
        self.letter = ""

    def setLetter(self, char):
        self.letter = char

    def addPlayer(self, id):
        self.players[id] = Player(id)

    def writeColumn(self, id, column, word):
        if word[0] != self.letter:
            return -1

        self.players[id].writeColumn(column, word)

    def setScore(self):
        for column in Gameboard.COLUMNS:
            for player in self.players:
                answer = self.players[player].gameboards[-1].columns[column]