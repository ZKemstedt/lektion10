import datetime

class KwargsToAttributes(type):
    def __call__(self, *args, **kwargs):

        # create a default type object
        obj = type.__call__(self, *args)

        # set kwargs as attributes
        for name, value in kwargs.items():
            setattr(obj, name, value)

        # return custom instantiated object
        return obj


class Person(object, metaclass=KwargsToAttributes):
    pass


new_person = Person(name = "Per", birthdate = datetime.date(1958, 10, 1))


print(new_person.name)
print(new_person.birthdate)


