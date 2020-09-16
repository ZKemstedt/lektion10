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
1 [, -a] -visa all hundar, om -A är givet så visas all information för varje hund
2, <refno> -visa all info om en hund
3, <ras>, <namn>, <ålder>, <ägare> -lägg till en hund
4, <refno> -ta bort en hund
5, <refno>, <nytt namn> -byt namn på en hund
6, <refno>, <nya ägarens namn> -byt namn på en hunds ägare
7, <refno>, <refno> -registrera en hunds bästa kompis
8, <nytt namn> -byt namn på hunddagisets chef

0 -stäng av programmet
'''


class Dog(object):
    """Represents a dog with several simple attributes."""

    def __init__(self, name: str, age: str, owner: str, breed: str) -> None:
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = breed
        self.friends = []

    def __str__(self) -> str:
        return f'''\t\t{self.name.title()}
    ras:   {self.breed}
    ålder: {self.age}
    ägare: {self.owner}
    bästa vänner: {', '.join([friend.name for friend in self.friends])}
        '''

    def add_friend(self, friend: object) -> None:
        """
        Add a best friend maximum one, golden-retriever may have many.
        
        Args:
            dog (Dog): A friendly Dog object
        """
        if not self.breed == 'golden-retriever' and self.friends:
            print(f'{self.name.title()} already has a best friend {self.friends[0].name.title()}')
            return
        self.friends.append(friend)
        print(f'Successfully registered {friend.name.title()} as a best friend of {self.name.title()}')

    def set_name(self, name: str) -> None:
        self.name = name

    def set_owner(self, owner: str) -> None:
        self.owner = owner


class DogDaycare(object):
    def __init__(self, name: str, boss_name: str) -> None:
        self.name = name
        self.boss_name = boss_name
        self.dogs = []

    def validate_dog(self, key: str) -> t.Union[Dog, None]:
        if key.isdigit():
            try:
                key = int(key) - 1
                dog = self.dogs[key]
            except IndexError:
                print(f'there\'s no dog at index {key}')
            except Exception as e:
                print(f'unknown error: {e}')
            else:
                return dog
            return None
        print('index must be an integer')
        return None

    def register_dog_friend(self, i: str, j: str) -> None:
        dog = self.validate_dog(i)
        friend = self.validate_dog(j)
        if dog and friend:
            dog.add_friend(friend)

    def add_dog(self, name: str, age: str, owner: str, breed: str) -> None:
        if age.isdigit():
            self.dogs.append(Dog(name, age, owner, breed))
        else:
            print('error: age must be an integer')

    def remove_dog(self, i: str) -> None:
        dog = self.validate_dog(i)
        if dog:
            self.dogs.remove(dog)
            print('successfully removed the dog')

    def set_dog_name(self, i: int, name: str) -> None:
        dog = self.validate_dog(i)
        if dog:
            dog.set_name(name)
            print('successfully updated the name')

    def set_boss_name(self, name: str) -> None:
        self.boss_name = name

    def list_dogs_short(self) -> None:
        print('index\tras\tnamn\tålder\tägare')
        for i, dog in enumerate(self.dogs):
            print(f'{i + 1}\t{dog.breed} \t{dog.name} \t{dog.age} \t{dog.owner}')

    # def list_dogs_long(self) -> None:
    #     pass  # not required, and I'm too tired to implement it right now

    def display_dog(self, i: str) -> None:
        dog = self.validate_dog(i)
        if dog:
            print(dog)

    def change_dog_owner(self, i: str, name: str) -> None:
        dog = self.validate_dog(i)
        if dog:
            dog.set_owner(name)
            print('successfully changed dog\'s owner')


def user_input() -> t.Tuple[str, ]:
    return input('>> ').lower().split(' ')


# 3 putte 35 jeppe bäver
#   Skapa en meny som frågar användaren om denne vill lägga till en ny hund, ta bort en hund, ändra chefsnamn,
#    ändra hundnamn, ändra hundägare osv eller skriva ut en lista på alla hundar som hunddagiset har.

if __name__ == '__main__':
    daycare = DogDaycare(name=NAME, boss_name='Zephyro')
    print(INSTRUCTIONS)
    while True:
        args = user_input()
        action = args.pop(0)    # identifies what to do
        if not args:
            if action == '0':
                break
            elif action == '1':
                daycare.list_dogs_short()
            elif action == '?':
                print(INSTRUCTIONS)
            elif not action:
                print('type 0 to exit, ? for help.')
        else:
            try:
                if action == '3':
                    daycare.add_dog(*args)
                elif action == '5':
                    daycare.set_dog_name(*args)
                elif action == '6':
                    daycare.change_dog_owner(*args)
                elif action == '7':
                    daycare.register_dog_friend(*args)
                # elif action == '1' and args == '-a':
                #     print('not implemented.')
                #     pass  # display all dogs long
                elif action == '2':
                    daycare.display_dog(*args) 
                elif action == '4':
                    daycare.remove_dog(*args)
                elif action == '8':
                    daycare.set_boss_name(*params)
            except TypeError as e:
                print(f'Error: {e}')  # invalid argument count

# TODO
# list -a
# fill in missing docstrings
# don't get overworked
