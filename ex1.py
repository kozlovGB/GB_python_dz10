import time
class TrafficLigh():
    def __init__(self):
        self.__color=""

    def ranning(self):
        while True:
            self.__color='красный'
            print(self.__color)
            time.sleep(1)
            self.__color = 'желтый'
            print(self.__color)
            time.sleep(1)
            self.__color = 'зеленый'
            print(self.__color)
            time.sleep(1)


ligh=TrafficLigh()
ligh.ranning()