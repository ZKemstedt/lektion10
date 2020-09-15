"""
a. Läsa in de två datafilerna.
b. Initiera en Table-instans med en lista med de lagnamn givna av teams.csv 
   som argument.
c. Iterera igenom alla matcher i PL_1819.csv och lägga till dem en och en i 
   Table-instansen så att denna kan uppdatera sina Team-instanser.
d. Efter var tionde match och efter den sista matchen för säsongen ska Table-
   instansen ombeds att skriva ut hela tabellställningen.
"""

import csv
from table import Table
from pathlib import Path

teams_file = Path('teams.csv')
matches_file = Path('PL_1819.csv')
assert teams_file.exists()
assert matches_file.exists()

with teams_file.open(mode='r') as f:
    table = Table(list(csv.reader(f))[0])

with matches_file.open(mode='r') as f:
    matches = list(csv.reader(f))
    matches.pop(0)
    for match in matches:
        print(table)
        table.register_match(*match)
        input('press enter to continue to next match')
