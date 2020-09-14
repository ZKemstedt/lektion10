class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        self._voltage = value


parrot = Parrot()

print(parrot.voltage)
parrot.voltage = 48
print(parrot.voltage)
