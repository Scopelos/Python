class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def bitum_mass(self, mass, thickness):
        result = self._length * self._width * mass * thickness
        print(result)

a = Road(5000, 20)
print(a._length)
print(a._width)
a.bitum_mass(25, 5)

