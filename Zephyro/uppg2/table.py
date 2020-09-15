"""
a. Initieras med en lista med lagnamn. Utifrån vart och ett av dessa lagnamn 
   ska en Team-instans skapas och läggas i en lista.
b. Ha en metod för att ta emot data från en match och uppdatera de lag som 
   matchen gäller.
c. Kunna skriva ut hela tabellställningen sorterad på poäng i fallande skala i
   formatet Lagnamn, Poäng, Målskillnad.
"""
from team import Team


class Table(object):

    def __init__(self, teams: list):
        self.teams = {}
        for team in teams:
            self.teams[team] = Team(team)

    def register_match(self, *data: str):
        try:
            date, team1, team2, score1, score2 = data
            score1, score2 = int(score1), int(score2)
        except Exception as e:
            print(f'Error: {e}')
            return
        if score1 > score2:
            self.teams[team1].win()
            self.teams[team2].loss()
        elif score1 == score2:
            self.teams[team1].even()
            self.teams[team2].even()
        else:
            self.teams[team1].loss()
            self.teams[team2].win()
        self.teams[team1].update_goals(score1-score2)
        self.teams[team2].update_goals(score2-score1)

    def __str__(self):
        teams = sorted(self.teams.values(), key=lambda t: t.points, reverse=True)
        text = 'Team'.ljust(25) + 'Points'.rjust(10) + 'goaldiff'.rjust(10) + '\n'
        text += '\n'.join([str(team) for team in teams])
        return text


# if __name__ == "__main__":
#     table = Table(['Manchester', 'AIK'])
#     table.register_match('asdf,Manchester,AIK,15,1')
#     print(table)
