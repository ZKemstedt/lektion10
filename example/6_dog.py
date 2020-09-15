"""
    1. Skapa en klass som heter Dog med attributen namn,
    ålder, ägare, ras, favoritleksak
    
    2. När man initialiserar (skapar) en ny instans av klassen
     (med init), kräv att man skriver in namn, ålder och ägare.
     Hunden behöver däremot inte ha en favoritleksak eller bästa
     hundkompis när den läggs till.
    
    3. Skapa en metod som heter set_name som ändrar hundens namn

    4. Skapa en metod som heter set_age som ändrar hundens ålder.

    5. skapa en metid som heter set_owner som ändrar hundens ägare.

    6. Skapa en metod som heter add_best_friend. Bästa hundkompisen ska
     vara en instans av objektet Dog. Antal bästa hundkompisar får vara max 1,
     men om det är en golden retriever får man ha hur många som helst. 
"""


class Dog:
    def __init__(self, name, age, owner, **kwargs):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = kwargs.get('breed', None)
        self.toy = kwargs.get('toy', None)
        self.friends = []
        friend = kwargs.get('friend', None)
        if(friend):
            self.friends.append(friend)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_owner(self, owner):
        self.owner = owner

    def add_best_friend(self, dog):
        """
            Add a best friend maximum one, golden retriever may have many.

            Args:
                dog (Dog): A friendly dog object
        """
        if(self.breed == "golden retriever"):
            self.friends.append(dog)
        else:
            self.friends = [dog]


a_dog = Dog("Fido", 4, "Robert", breed="golden retriever")

a_dog.add_best_friend(Dog("Felix", 10, "Sorlin", breed="bulldog"))
a_dog.add_best_friend(Dog("Rocky", 10, "Sorlin", breed="bulldog"))

for dog_friend in a_dog.friends:
    print(dog_friend.name)
