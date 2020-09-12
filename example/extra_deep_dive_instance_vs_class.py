import types
import inspect

# A class
class Car(object):
    def a_method(self):
        pass


functions = list(filter(lambda x: isinstance(getattr(Car, x), (types.FunctionType)), dir(Car)))
methods = list(filter(lambda x: isinstance(getattr(Car, x), (types.MethodType)), dir(Car)))
print((
    f"Car printed {Car}\n"
    f"Car isclass {inspect.isclass(Car)}\n"
    f"Car is of type {type(Car)}\n"
    f"Car has functions: {functions}\n"
    f"Car has methods: {methods}\n"
    ))

# A instance of a class
a_car = Car()
functions = list(filter(lambda x: isinstance(getattr(a_car, x), (types.FunctionType)), dir(a_car)))
methods = list(filter(lambda x: isinstance(getattr(a_car, x), (types.MethodType)), dir(a_car)))

print((
    f"a_car printed {a_car}\n"
    f"a_car isclass {inspect.isclass(a_car)}\n"
    f"a_car is of type {type(a_car)}\n"
    f"a_car has functions: {functions}\n"
    f"a_car has methods: {methods}\n"
    ))