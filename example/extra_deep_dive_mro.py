class Base:
    def __init__(self):
        print(self.__class__.mro())


class X(Base):
    def method(self):
        print("X")


class Y(Base):
    def method(self):
        print("Y")


class A(Y):
    pass


class B(A):
    pass


class C(B, X):
    pass


C().method()
