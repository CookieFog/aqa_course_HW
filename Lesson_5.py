# Homework_5 Lesson_5 --------------------------------------------------------------------------------------------------

import math


class SqrtError(Exception):
    pass


try:
    s = float(input("Please choose positive number!"))
    if s < 0:
        raise SqrtError("Error!. For sqrt you can use only positive number")
    else:
        print(math.sqrt(s))

finally:

    print("Calculation process has ended")
