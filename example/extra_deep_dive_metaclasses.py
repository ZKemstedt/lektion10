import datetime


class A():
    pass


# A default class has the type type
print(f'Type of A: {type(A)}')


class KwargsToAttributes(type):
    def __call__(cls, *args, **kwargs):

        # create a default type object
        obj = type.__call__(cls, *args)

        # set kwargs as attributes
        for name, value in kwargs.items():
            setattr(obj, name, value)

        # return custom instantiated object
        return obj


class Person(object, metaclass=KwargsToAttributes):
    pass


new_person = Person(name="Per", birthdate=datetime.date(1958, 10, 1))

# A class with a metaclass can have a custom type
print(f'Type of Person: {type(Person)}')

# The metaclass sets class attributes from kwargs
print(f'Attribute name: {new_person.name}')
print(f'Attribute birthdate: {new_person.birthdate}')
