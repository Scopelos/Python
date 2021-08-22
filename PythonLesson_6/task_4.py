class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Текущая скорость машины", self.speed, "км/ч.")

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        print("Машина повернула", direction)


# class Position(Worker):
#     def __init__(self, name, surname, _income):
#         super().__init__(name, surname, _income)

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f"Текущая скорость машины", self.speed, "км/ч.")
        if self.speed > 60:
            print("Скорость превышена!")


class SportsCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость машины", self.speed, "км/ч.")
        if self.speed > 40:
            print("Скорость превышена!")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

a = Car(10, "red", "Nissan")
a.go()
print(a.speed)
a.show_speed()
a.turn("направо")
print(a.is_police)
a.stop()

b = TownCar(75, "grey", "Lincoln")
b.show_speed()
print(b.color)

c = WorkCar(45, "white", "Kia")
c.show_speed()
print(c.name)

d = PoliceCar(150, "black", "Ford")
print(d.speed)
print(d.is_police)