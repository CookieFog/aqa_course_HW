# Homework_task_1
# class House:
#     """House street parameter"""
#
#     def __init__(self, street: str):
#         self.street = street
#
#     @property
#     def parameters(self):
#         print(f'{self.street} is a street')
#         return self.street
#
#     @parameters.setter
#     def parameters(self, New_street):
#         self.street = New_street
#         print(f'Old street was changed. New street is now "{New_street}')
#
#
# if __name__ == '__main__':
#     house = House("Ryikivska")
#
#
# house.parameters = 'Perejaclavckaja'
#
# print(house.parameters)

# Homework_task_2

class House:
    """House street parameter"""

    def __init__(self, street: str):
        self.street = street

    @property
    def parameters(self):
        print(f'{self.street} is a street')
        return self.street

    @parameters.setter
    def parameters(self, New_street):
        self.street = New_street
        print(f'Old street was changed. New street is now "{New_street}')


if __name__ == '__main__':
    house = House("Ryikivska")

house.parameters = 'Perejaclavckaja'


class city(House):
    """Current location of the house"""

    def __init__(self, city74):
        super().__init__(self.street)
        self.city74 = city74

print(city)






# class House:
#     """House parameters"""
#
#     def __init__(self, street: str, age: int, House_number: int):
#
#         self.street = street
#         self.age = age
#         self.House_number = House_number
#
#     @property
#     def parameters(self):
#         print(f'{self.street}, {self.age}, {self.House_number} is a parameters of the house')
#         return self.street, self.age, self.House_number
#
#     @parameters.setter
#     def parameters(self, New_street):
#         self.street = New_street
#         print(f'Old street was changed street is now "{New_street}')
#
#     def parameters_1(self, New_age):
#         self.age = New_age
#         print(f'Old age was changed street is now "{New_age}')
#
# if __name__ == '__main__':
#     house = House("Ryikivska", 32, 43)
#
# house.parameters = ('Perejaclavckaja')
# house.parameters_1 = ('54')
# print(house.parameters)

# class Fruit:
#     def __init__(self, name: str):
#         self._name = name
#
#     @property
#     def fruit_name(self):
#         print(f'"{self._name}" was done')
#         return self._name
#
#     @fruit_name.setter
#     def fruit_name(self, value):
#         print(f'{self._name} is now "{value}')
#         self._name = value
#
#
# if __name__ == "__main__":
#     fruit = Fruit('Banana')
#
# fruit.fruit_name = "orange"
#
# print(fruit.fruit_name)
