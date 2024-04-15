class House:
    """House parameters"""

    def __init__(self, street: str):
        self.street = street

    @property
    def parameters(self):
        print(f'{self.street} is a street')
        return self.street

    @parameters.setter
    def parameters(self, New_street):
        self.street = New_street
        print(f'{self.street} old street was changed street is now "{New_street}')


if __name__ == '__main__':
    house = House("Ryikivska")


house.parameters = 'Perejaclavckaja'

print(house.parameters)























































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
