
class SingleTone(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            instance = super().__call__(*args, **kwargs)
            cls.__instance[cls] = instance
        return cls.__instance[cls]


class DoD(metaclass=SingleTone):
    def __init__(self, triangle_width, triangle_length, triangle_height):
        self.triangle_width = triangle_width
        self.triangle_length = triangle_length
        self.triangle_height = triangle_height


dod_1 = DoD(15, 544, 544)
dod_2 = DoD(13, 533, 533)

print(dod_1 is dod_2)





