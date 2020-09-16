import cmd


dogs = []


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

    def __str__(self):
        return f"{self.name}"

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


def create_dog(arg):
    try:
        dogs.append(Dog(*parse(arg)))
    except Exception as e:
        print(f'Failed creating dog {e}')


def list_dogs():
    print("\n".join(map(str, dogs)))


class DogShell(cmd.Cmd):
    intro = 'Welcome to the dog shell.   Type help or ? to list commands.\n'
    prompt = '(dog) '

    # ----- basic dog commands -----
    def do_create(self, arg):
        'Create a dog'
        create_dog(arg)

    def do_list(self, arg):
        'List all dogs'
        list_dogs()

    def do_bye(self, arg):
        'Stop program, close the dog window, and exit:  BYE'
        print('Thank you for using dog')
        return True

    def precmd(self, line):
        line = line.lower()
        return line


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(arg.split())


if __name__ == '__main__':
    DogShell().cmdloop()
