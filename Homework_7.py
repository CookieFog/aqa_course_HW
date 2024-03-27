# Homework_7_1
# def func_map(func, iterable_obj: list):
#     for item in iterable_obj:
#         yield func(item)
#
#
# def func_filter(func, iterable_obj: list):
#     for item in iterable_obj:
#         if func(item):
#             yield func(item)


# Homework_7_2

# def DOD(x: int):
#     return lambda y: pow(x, y)
#
#
# def test(arg):
#     if callable(arg):
#         print('start')
#         print(arg(2))  # pow(x, y)
#         print('finish')
#     else:
#         print("Hm, something went wrong!")
#
#     test(DOD(10))
#
#     print("Error544")


# Homework_7_3
# **************************
# def print_hi():
#     result = 'Hi'
#     return result
#
#
# def print_bye():
#     result = 'Bye'
#     return result
#
#
# def sum_of_numbers():
#     result = 5 + 6
#     return result
#
#
# func_name = input('Please, enter function name: ')
# try:
#     print(eval(func_name))
# except NameError:
#     print('There is no such function')


# **************************
def print_hi():
    print("Hi")


def print_bye():
    print("Bye")


def evaluate():
    user_input = input("Please enter print_hi() or print_bye()")
    eval(user_input)


evaluate()
# **************************