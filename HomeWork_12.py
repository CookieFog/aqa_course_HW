# HomeWork_12_1
from abc import ABC, abstractmethod


class AbstractDevice(ABC):
    def __init__(self):
        print(f'This is AbstractDevice')

    @abstractmethod
    def turn_on(self):
        print(f'abstract_device is now on')

    def turn_off(self):
        print(f'abstract_device is now off')


class ConcreteDevice(AbstractDevice):
    def turn_on(self):
        return "Abstract_device is now on"

    def turn_off(self):
        return "Abstract_device is now off"


Class = ConcreteDevice()
print(Class.turn_on())
print(Class.turn_off())


# HomeWork_12_2

class TV:
    def __init__(self):
        self.type = 'Panasonic'

    def turn_on(self):
        print(f'TV system is now ON')

    def turn_off(self):
        print(f'TV system is now OFF')


class Lights:

    def __init__(self):
        self.type = 'Lamps'

    def turn_on(self):
        print(f'Lamps system is now ON')

    def turn_off(self):
        print(f'Lamps system is now OFF')


class Heating:

    def __init__(self):
        self.type = 'House Heating'

    def turn_on(self):
        print(f'Heating system is now ON')

    def turn_off(self):
        print(f'Heating system is now OFF')


class HomeFacade:

    def __init__(self):
        self.__TV = TV()
        self.__Lights = Lights()
        self.__Heating = Heating()

    @property
    def TV(self):
        return self.__TV

    @property
    def Lights(self):
        return self.__Lights

    @property
    def Heating(self):
        return self.__Heating

    def come_home(self):
        self.TV.turn_on()
        self.Lights.turn_on()
        self.Heating.turn_on()

    def go_out(self):
        self.TV.turn_off()
        self.Lights.turn_off()
        self.Heating.turn_off()


house = HomeFacade()
house.come_home()
house.go_out()


# HomeWork_12_3

class MyContextManager:

    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(file=self.file_path, mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


path = 'C:/Users/user/Desktop/test_file.csv'

with MyContextManager(file_path=path, mode='r') as file:
    print(file.readlines())
