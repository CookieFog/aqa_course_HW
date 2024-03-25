import math

# Homework_lesson_6 #1 date 17.03.2024
# def sum_range(start, end):
#     if start > end:
#         end, start = start, end
#     return sum(range(start, end + 1))
#
#
# print(sum_range(4, 15))

# Homework_lesson_6 #2 date 17.03.2024

# def square(x):
#     y = 2
#     print('периметр квадрата (P)', '=', x * 4)
#     print('площа квадрата (S)', '=', pow(x, y))
#     print('діагональ квадрата (d)', '=', math.sqrt(2)*x)
#
#
# square(3)

# Homework_lesson_6 #3 date 17.03.2024

# ************************************
# dictionary = "{'key': 'value'}"
# print(type(dictionary))
# res_of_upper = dictionary.upper()
# print(res_of_upper)
# result = eval(dictionary)
# print(type(result))
#
#
# def check_data_type(data: str):
#     try:
#         return type(eval(data))
#     except:
#         pass
#
#
# result = eval('check_data_type({})')

# **********************************
# value = input("something to write")
#
#
# result = eval(value)
# print(type(result))
#
#
# def check_data_type(data: str):
#     try:
#         return type(eval(data))
#     except:
#         pass
#


user_input = input("something to write")


def check_data_type(data: str):
    try:
        result = eval(data)
        print(f"User is going to work with {type(result).__name__}")
    except Exception as e:
        print(f'Something went wrong. {e}')


result = eval('check_data_type({})')
