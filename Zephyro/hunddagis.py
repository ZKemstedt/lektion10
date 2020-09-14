
# Uppgiftsbeskrivning

# Vägledning del 1: Hund

# Din närmaste granne är ett hunddagis. De har nu bett dig om hjälp att skapa ett hundregister så att de kan
# hålla koll på alla sina hundar. Hunddagiset funderar på att öppna upp på fler ställen i stan i framtiden, så
# varje hunddagis måste ha sitt eget register med de hundar som går på det dagiset.
# Varje hund har ett namn, ålder, ägare, ras, favoritleksak och en bästa hundkompis. Golden retrievers är dock
# så pass sociala att de kan ha flera bästa hundkompisar.
# Det ska gå att
# lägga till nya hundar till registret,
# ta bort hundar från registret,
# uppdatera namnet på hunden
# samt lägga till en bästa hundkompis till varje hund.
# Om rasen INTE är golden retriever så ska ett felmeddelande skrivas ut när man försöker lägga till en
# till hundkompis.

# Vägledning del 1: Hund
# 1. Skapa en klass som heter Dog med attributen namn, ålder, ägare, ras, favoritleksak
# 2. När man initialiserar(skapar) en ny instans av klassen(med init), kräv att man skriver in namn, ålder och
#    ägare. Hunden behöver däremot inte ha en favoritleksak eller bästa hundkompis när den läggs till.
# 3. Skapa en metod som heter set_name som ändrar hundens namn
# 4. Skapa en metod som heter set_age som ändrar hundens ålder.
# 5. Skapa en metod som heter set_owner som ändrar hundens ägare
# 6. Skapa en metod som heter add_best_friend. Bästa hundkompisen ska vara en instans av objektet Dog. Antal bästa
#    hundkompisar får vara max 1, men om det är en golden retriever får man ha hur många som helst.

# Vägledning del 2: Hunddagis.
# 1. Skapa en klass som heter Dog_daycare
# 2. När man initialiserar en ny instans av klassen, kräv att man skriver in namn på dagiset samt namn på chefen
#    för dagiset.
# 3. Vid initialisering ska en ny, tom lista skapas, där du sedan lägger dina hundar.
# 4. Lägg till metoderna add_dog, remove_dog, set_boss_name.

# Utanför dina två klasser Dog_daycare, och Dog:
# 1. Skapa en instans av klassen Dog_daycare som heter ”Vacker Tass”
# 2. Skapa en meny som frågar användaren om denne vill lägga till en ny hund, ta bort en hund, ändra chefsnamn,
#    ändra hundnamn, ändra hundägare osv eller skriva ut en lista på alla hundar som hunddagiset har.

import typing as t

#
# Version 1
# lista av hundar, referera till hund by list index (+1)
#

NAME = 'Vacker Tass'
INSTRUCTIONS = '''
    ~ Hunddagiset Vacker Tass ~
En kort fin menig, typ en slogan

[instructioner/alternativ]
1 [-a] -visa all hundar, om -A är givet så visas all information för varje hund
2 <refno> -visa all info om en hund
3 <ras> <namn> <ålder> <ägare> -lägg till en hund
4 <refno> -ta bort en hund
5 <refno> <nytt namn> -byt namn på en hund
6 <refno> <nya ägarens namn> -byt namn på en hunds ägare
7 <refno> <refno> -registrera en hunds bästa kompis
8 <nytt namn> -byt namn på hunddagisets chef

0 -stäng av programmet
'''


class Dog(object):
    """"""
    def __init__(self, race: str, name: str, age: str, owner: str):
        self.name = name
        self.age = age
        self.owner = owner
        self.race = race
        self.best_friends = []

    def __str__(self):
        return f'''\t\t{self.name.title()}
    ras:   {self.race}
    ålder: {self.age}
    ägare: {self.owner}
    bästa vänner: {''.join([friend.name for friend in self.best_friends])}
        '''

    def add_best_friend(self, friend) -> None:
        if not self.race == 'golden-retriever' and self.best_friends:
            print(f'{self.name.title()} already has a best friend {self.best_friends[0].name.title()}')
            return
        self.best_friends.append(friend)
        print(f'Successfully registered {friend.name.title()} as a best friend of {self.name.title()}')

    def set_name(self, name: str) -> None:
        self.name = name


class DogDaycare(object):
    """"""
    def __init__(self, name: str, boss_name: str):
        self.name = name
        self.boss_name = boss_name
        self.dogs = []

    def __str__(self):
        """Returns a string containing info about the daycare"""
        pass  # not required, and I'm too tired to implement it right now

    def register_dog_friend(self, *args) -> None:
        if len(args) != 2:
            print('`register_dog_friend`: invalid argument count')
            return
        try:
            i = int(args[0]) - 1
            fi = int(args[1]) - 1
            friend = self.dogs[fi]
        except ValueError:
            print(f'`register_dog_friend`: dog identifiers must be integers {args[0]} {args[1]}')
            return
        except IndexError:
            print(f'`register_dog_friend`: there\'s no dog (friend) with index {fi}')
            return
        try:
            self.dogs[i].add_best_friend(friend)
        except IndexError:
            print(f'`register_dog_friend`: there\'s no dog with index {i}')
            return

    def add_dog(self, *args):
        try:
            dog = Dog(*args)
        except Exception as e:
            print('`add_dog`: invalid constructor arguments')
            print(f'`add-dog`: exception: {e}')
        else:
            self.dogs.append(dog)

    def remove_dog(self, i):
        try:
            del self.dogs[int(i) + 1]
        except ValueError:
            print(f'`remove_dog`: identifier must be an integer {args[0]}')
        except IndexError:
            print(f'`remove_dog`: there\'s no dog with index {args[0]}')

    def set_dog_name(self, *args):
        if len(args) < 2:
            print('`set_dog_name`: invalid argument count')
            return
        if len(args) > 2:
            # that's a long name >.>
            new_name = ' '.join(args[1:])
        else:
            new_name = args[1]
        try:
            i = int(args[0]) - 1
            self.dogs[i].set_name(new_name)
            print('sucessfully updated the name')
        except ValueError:
            print(f'`set_dog_name`: identifier must be an integer {args[0]}')
        except IndexError:
            print(f'`set_dog_name`: there\'s no dog with index {args[0]}')

    def set_boss_name(self, name: str, *names: t.Optional[t.List[str]]) -> None:
        if names:
            name += ' ' + ' '.join(names)  # space before and between extra names
        self.boss_name = name

    def list_dogs_short(self) -> None:
        print('index\tras\tålder\tnamn\tägare')
        for i, dog in enumerate(self.dogs):
            print(f'{i + 1}\t{dog.race} \t{dog.name} \t{dog.age} \t{dog.owner}')

    def list_dogs_long(self):
        pass  # not required, and I'm too tired to implement it right now

    def display_dog(self, i: str) -> None:
        try:
            print(self.dogs[int(i) - 1])
        except ValueError:
            print(f'`display_dog`: identifier must be an integer {args[0]}')
        except IndexError:
            print(f'`display_dog`: there\'s no dog with index {args[0]}')

    def change_dog_owner(self, *args) -> None:
        if len(args) < 2:
            print('`change_dog_owner`: invalid argument count')
        if len(args) > 2:
            # that's a long name >.>
            new_name = ' '.join(args[1:])
        else:
            new_name = args[1]
        try:
            i = int(args[0]) - 1
            self.dogs[i].set_owner(new_name)
        except ValueError:
            print(f'`change_dog_owner`: identifier must be an integer {args[0]}')
        except IndexError:
            print(f'`change_dog_owner`: there\'s no dog (friend) with index {args[0]}')


def user_input() -> t.Tuple[str, ]:
    return input('>> ').lower().split(' ')


# 3 bäver putte 35 jeppe
#   Skapa en meny som frågar användaren om denne vill lägga till en ny hund, ta bort en hund, ändra chefsnamn,
#    ändra hundnamn, ändra hundägare osv eller skriva ut en lista på alla hundar som hunddagiset har.

if __name__ == '__main__':
    daycare = DogDaycare(name=NAME, boss_name='Zephyro')
    print(INSTRUCTIONS)
    while True:
        args = user_input()
        action = args[0]    # identifies what to do
        if len(args) < 2:
            if action == '0':
                break                       # '0' DONE
            elif action == '1':
                daycare.list_dogs_short()   # '1' DONE
            elif action == '?':
                print(INSTRUCTIONS)         # '?' DONE
            elif not action:
                print('type 0 to exit, ? for help.')    # '' Done
            continue    # all other actions require at least 2 parameters

        params = args[1:]   # parameters to pass
        if action == '1' and params[0] == '-a':
            print('not implemented.')
            pass  # display all dogs long
        elif action == '2':
            daycare.display_dog(params[0])  # '2' DONE
        elif action == '3':
            daycare.add_dog(*params)         # '3' DONE
        elif action == '4':
            daycare.remove_dog(params[0])   # '4' DONE
        elif action == '5':
            daycare.set_dog_name(*params)   # '5' DONE
        elif action == '6':
            daycare.change_dog_owner(*params)  # '6' DONE
        elif action == '7':
            daycare.register_dog_friend(*params)  # '7'DONE
        elif action == '8':
            daycare.set_boss_name(params)   # '8' DONE

# TODO
# list -a
# fill in missing docstrings
# fix inconsistent use of typing / annotations
# make a real handler-method and/or parser in daycare for applying actions on dog objects
#   lookup dog by name
#   lookup dog by owner
#   lookup dog by race
#   change order in the if-chain to check for argument lenth
#   change argument-splitter from space to comma (handle names with spaces)
# don't get overworked
