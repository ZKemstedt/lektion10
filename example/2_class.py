'''
Type hierarchy - Custom classes
    - Can be created by class definition
    see [https://docs.python.org/3/reference/compound_stmts.html#class-definitions]

    classdef    ::=  [decorators] "class" classname [inheritance] ":" suite
    inheritance ::=  "(" [argument_list] ")"
    classname   ::=  identifier
'''


# Class definitions

# Custom class without inheritance (default is object)
class Vehicle:
    pass


# Custom class written with default inheritance
class Person(object):
    pass


# Custom class with inheritance and a function definition
class Car(Vehicle):
    def honk(self):
        print("honk")


print(Car)  # <class '__main__.Car'> a class object

'''
Class objects support two kinds of operations: attribute references and instantiation.
see: [https://docs.python.org/3/tutorial/classes.html#class-objects]
'''


# 1. What is a attribute references?
class Calculator:
    c = 0  # Attribute reference (a variable)

    def hello_world(self):  # Attribute reference (a function)
        Calculator.c += 1
        print(f'hello world called {Calculator.c} times.')


# 2. What is instantiation?
c1 = Calculator()  # when we call () a class we will create a Class instance, a instance of the class Calculator.
c2 = Calculator()  # We can create multiple instances and bind names to them c1, c2 etc.


'''
In the Type hierarchy we can find the Callable type and read that Classes are callable.
EXERCISE: Do you recognize any other Callable types?

Type hierarchy - Callable type
    - The Callable types can be used with call operation "()" i.e func_name()
    see [https://docs.python.org/3/reference/expressions.html#calls]

    - Instance methods
    - Classes
'''
# when we define functions in a class and that class is instantiated, they are called instance methods.
# i.e when you have:

a_list = [1, 4, 2, 5]
a_list.sort()  # This is a built-in method

# with our custom class we defined the function that will become a instance method: "hello_world"
c1.hello_world()  # hello world called 1 times.
c2.hello_world()  # hello world called 2 times.

# notice that the state is shared when you use a class attribute reference

'''
class Calculator:
    c = 0  # Attribute reference (a variable)

    def hello_world(self):  # Attribute reference (a function)
        Calculator.c += 1
        print(f'hello world called {Calculator.c} times.')
'''


class IndependentCalculator:
    def __init__(self):  # init is called when you instantiate a class
        self.c = 0  # This is in the instance scope

    def hello_world(self):
        self.c += 1
        print(f'hello world called {self.c} times.')


ic = IndependentCalculator()  # a instance is created
ic.hello_world()  # hello world called 1 times.
ic.hello_world()  # hello world called 2 times.

ic2 = IndependentCalculator()  # another instance is created
ic2.hello_world()  # hello world called 1 times. ic2 instance is independent from ic instance

# EXERCISE what's happens if you construct a class with both a attribute variable and a instance variable with self?
# tips: construct a method that print the same self.variable_name
'''
class A:
    a = 0

    def a_method(self):
        print(self.a)


print(A.a)  # here we print(<class_name>.<variable_name>)
print(A().a_method())  # here we print self.<variable_name>) in the instance method
'''


# Extra reading:
# More about classes see examples at: [https://docs.python.org/3/tutorial/classes.html#classes]
# More about __init__ and basic customization of classes
# see: [https://docs.python.org/3/reference/datamodel.html#basic-customization}]
