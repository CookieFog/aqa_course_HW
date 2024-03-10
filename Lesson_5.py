# Homework_5_1 Lesson_5 ------------------------------------------------------------------------------------------------

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

# import math
#
#
# value = 0
# while value < 2:
#
#     try:
#         s = float(input("Please choose positive number!"))
#         if s < 0:
#             value += 1
#             raise SqrtError("Error!. For sqrt you can use only positive number")
#
#         else:
#             print(math.sqrt(s))
#             break
#     except ValueError as error:
#         print("value error. Please choose correct number!")
#         value += 1
#
#     finally:
#         print("Calculation process has ended")

# Homework_5_3 Lesson_5-------------------------------------------------------------------------------------------------

import sys

value = 0
while value < 2:
    try:
        first_number = float(input("Please enter first number for calculation process"))
        # if first_number == 'q':
        #     sys.exit("You chose to quit the program. GoodBye ")

        operator = input("Please choose operator")
        second_number = float(input("Please enter second number for calculation process"))

        if operator == "+":
            print(first_number + second_number)
            value += 1
        elif operator == "-":
            print(first_number - second_number)
            value += 1
        elif operator == "*":
            print(first_number * second_number)
            value += 1
        elif operator == "/":
            print(first_number / second_number)
            value += 1

    except ZeroDivisionError as error:

        print("Operation failed. Please enter right number! ZeroDivisionError")

    except ValueError as error:
        print("Operation failed please enter valid value")

    else:
        print("OK")
    finally:
        print("Calculator version 3.2")
    # reboot_calculation = input("For reboot calculation program press F. For end calculation program press Exit")
    # if reboot_calculation == 'F':
    #     print("OK")
    # if reboot_calculation == 'Exit':
    #     sys.exit("You chose to quit the program. GoodByE!")
