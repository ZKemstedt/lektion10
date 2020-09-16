# TODO This example is not completed
class Clothes:
    __type = {}

    def __init__(self):
        self.used = 0
        self.color = "Blue"

    def need_wash(self):
        return self.used > self.type[self.t]

    def use(self, times=1):
        self.used += times


class Pants(Clothes):
    __type = {"jeans": 3, "chinos": 10, "shorts": 5}

    def __init__(self, t):
        super().__init__()
        if(t in self.__type.keys()):
            self.t = t
        else:
            self.t = None

    def add_type(self, t, w):
        self.__type[t] = w

    def print_type(self):
        print(f"My type of pants are: {self.t}")


class UsedPants(Clothes):
    def __init__(self, used):
        self.used = 0


my_pants = Pants("jeans")

my_pants.use(4)
print(my_pants.need_wash())

my_pants.add_type("slacks", 10)
my_slacks = Pants("slacks")
my_slacks.use(9)
print(my_slacks.need_wash())
