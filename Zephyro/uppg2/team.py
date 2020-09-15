"""
    a. Initieras med ett lagnamn som ska sparas som ett klassattribut.
    b. Klassen ska även innehålla data om lagets poäng och målskillnad.
    c. Klassen ska ha en metod som kan användas till att uppdatera lagets data 
    efter att en match har spelats. Om laget har vunnit ska poängen öka med 3, 
    om matchen har slutat oavgjort ska poängen öka med 1 och vid förlust ska 
    poängen förbli oförändrad.
"""


class Team(object):

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goaldiff = 0
        # self.history = []

    def __str__(self):
        points = str(self.points)
        goals = str(self.goaldiff)
        return f'{self.name.ljust(25)}{points.rjust(10)}{goals.rjust(10)}'

    def update_goals(self, diff: int):
        self.goaldiff += diff

    def loss(self):
        pass

    def win(self):
        self.points += 3

    def even(self):
        self.points += 1


# if __name__ == '__main__':
#     man = Team('Manchester')
#     man.even()
#     man.update_goals(-1)  # 3 - 0
#     print(man)
