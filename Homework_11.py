class House:
    """House parameters"""

    def __init__(self, street, number, age):
        self.street = street
        self.number = number
        self.age = age

    def build(self):
        print('House street' + str(self.street) + "House number" + str(self.number) + "House age" + str(self.age))


House_1 = House("Ryikivska", 20, 5)
House_2 = House("Ryikivasa", 32, 10)

print(House_2.number)

House_1.build()