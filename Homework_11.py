# Homework_task_1
# class House:
#     """House parameters"""
#
#     def __init__(self, street: str, age: str, number: str):
#         self.street = street
#         self.age = age
#         self.number = number
#
#     @property
#     def parameters(self):
#         print(f'{self.street} is a street, {self.age} is age, {self.number} is a number of the house')
#         return self.street, self.age, self.number
#
#     # @parameters.setter
#     # def parameters(self, new_street: dict):
#     #     self.street = new_street
#     #     print(f'Old street was changed. New street is now "{new_street}')
#
#     def setter_parameters(self, new_street, new_age, new_number):
#         self.street = new_street
#         self.age = new_age
#         self.number = new_number
#         print(f"Old parameters was changed. New parameters street is {new_street}, age is {new_age}, number is "
#               f"{new_number}")
#
#
# house = House("Kiev", '32', '43')
# house.setter_parameters('Kiev', '10', '18')
#
# # print(house.setter_parameters('Kiev', '10', '15'))
#
# print(house.parameters)

# Homework_task_2

class House:
    """House parameters"""

    def __init__(self, street: str, age: str, number: str):
        self.street = street
        self.age = age
        self.number = number

    @property
    def parameters(self):
        print(f'{self.street} is a street, {self.age} is age, {self.number} is a number of the house')
        return self.street, self.age, self.number

    def setter_parameters(self, new_street, new_age, new_number):
        self.street = new_street
        self.age = new_age
        self.number = new_number
        print(f"Old parameters was changed. New parameters street is {new_street}, age is {new_age}, number is "
              f"{new_number}")


# house = House("VelucaPonasivka", '32', '43')
# house.setter_parameters('Kiev', '10', '18')
# print(house.setter_parameters('Kiev', '10', '15'))
# print(house.parameters)


class CityLive(House):
    """City parameters"""

    def __init__(self, street, age, number, city_name, current_house_location, other_information):
        super().__init__(street, age, number)
        self.city_name = city_name
        self.current_house_location = current_house_location
        self.other_information = other_information

    @property
    def city_parameters(self):
        print(f"{self.city_name} is the city name, {self.current_house_location} is current house location, "
              f"{self.other_information} is other information to add")
        return self.city_name, self.current_house_location, self.other_information

    def information_parameters_deleter(self):
        print(f'{self.city_name}, {self.current_house_location}, {self.other_information} was deleted!')
        del self.city_name, self.current_house_location, self.other_information


city = CityLive("Pich_street", '100', '17', 'London',
                'London_Pich_street', 'None')

city.setter_parameters('Pich_street', '100', '17')
print(city.city_parameters)
print(city.parameters)


