# Homework_5_1 Lesson_5 -----------------------------------------------------------------------------------------------

# import math
#
#
# class SqrtError(Exception):
#     pass
#
#
# try:
#     s = float(input("Please choose positive number!"))
#     if s < 0:
#         raise SqrtError("Error!. For sqrt you can use only positive number")
#     else:
#         print(math.sqrt(s))
#
# finally:
#
#     print("Calculation process has ended")


# Homework_5_2 Lesson_5-------------------------------------------------------------------------------------------------

import math


class SqrtError(Exception):
    pass


value = 0
while value < 2:

    try:
        s = float(input("Please choose positive number!"))
        if s < 0:
            value += 1
            raise SqrtError("Error!. For sqrt you can use only positive number")

        else:
            print(math.sqrt(s))
            break
    except ValueError as error:
        print("value error. Please choose correct number!")
        value += 1

    finally:
        print("Calculation process has ended")
