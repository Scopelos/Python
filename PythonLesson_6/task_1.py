from time import sleep


class TrafficLight:
    modes = [("красный", 7), ("жёлтый", 2), ("зелёный", 8)]

    def __init__(self):
        self.__color = self.modes[0][0]
        print("Светофор начинает работу")
        sleep(1)
        while True:
            self.running()

    def running(self):
        for i in range(100):
            for mode in self.modes:
                color, period = mode
                self.__color = color
                print(self.__color)
                sleep(period)


light = TrafficLight()
print(" Функция 'sleep' - это 'помощь зала'")

