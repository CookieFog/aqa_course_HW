# Homework task #1 date 07.03.2024------------------------------------------------------------------------
# list_1 = ["john", "marta", "james", "amanda", "marianna"]
#
# for names in list_1:
#     print(names.capitalize())
# Homework task #2 date 07.03.2024------------------------------------------------------------------------
# list_3 = ["FirstItem", "FriendsList", "MyTuple"]


# Homework task #3 date 07.03.2024------------------------------------------------------------------------
# dictionary_1 = {'PHP': 'PHP creator is Rasmus Lerdorf', 'Python': 'Python creator isGuido van Rossum',
# 'C++': 'C++ creator is Björn Stroustrup', 'C#': 'C# creator isDennis Ritchie'
#                 }
# for names in dictionary_1:
#
#     print(dictionary_1.get('PHP'), ". NO it isn't!")
#     print("My favorite programming language is Python. It was created by Guido van Rossum.")
#     print(dictionary_1.get('Python'), ". Yes this is it:)")
#     print(dictionary_1.get('C++'), ". NO it isn't!")
#     print("My favorite programming language is Python. It was created by Guido van Rossum.")
#     print(dictionary_1.get('C#'), ". NO it isn't!")
#     break
# print("My favorite programming language is Python. It was created by Guido van Rossum.")
# del dictionary_1['PHP']
# print(dictionary_1)
# Homework task #4 date 07.03.2024-------------------------------------------------------------------------
# list_4 = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# for names in list_4:
#     if names is type(str):
#         print(list_4[1])
#
#     continue

# Homework task #5 date 09.03.2024-------------------------------------------------------------------------
# types = [1, 10, 2, 12, {'key': 'value'}]    # Please choose any value in field {'key': 'value'} example 544
# for value in types:
#     if (isinstance(types[0], int) and isinstance(types[1], int)
#             and isinstance(types[2], int) and isinstance(types[3], int) and isinstance(types[4], int)):
#         print("True")
#         print(value)
#         continue
#     else:
#         print("loop 'For' is not working with float. This program working only with int! ")
#         print("!unexpected error loop is closed!")
#     break
# Homework task #6 date 09.03.2024---------------------------------------------------------------------------
# dict_1 = input("awaiting letter")
# dictionary = {'Special characters': 0, 'letters': 0, 'numbers': 0}
#
# for x in dict_1:
#     if x.isalpha():
#         dictionary['letters'] += 1
#     elif x.isdigit():
#         dictionary['numbers'] += 1
#     else:
#         dictionary['Special characters'] += 1
# ", ".join(dictionary)
#
# print(", ".join(dictionary))

# dict_1 = input("awaiting letter")
# dictionary = {}
#
# for i in dict_1:
#     if i in dict_1:
#         dictionary['Letters'] += 1
# ", ".join(dictionary)
#
# print(", ".join(dictionary))

# # Homework task #7 date 10.03.2024----------------------------------------------------------------------------
# value = 0
# while value < 2:
#     try:
#         print("Welcome to calculator version 2.1. Warning you have only 2 attempts and after that program will close!")
#         first_number = float(input("Please choose first number"))
#         base_operator = input("Please choose operator")
#         second_number = float(input("Please choose second number"))
#
#         if base_operator == "+":
#             print(first_number + second_number)
#             break
#         elif base_operator == "-":
#             print(first_number - second_number)
#             break
#         elif base_operator == "/":
#             print(first_number / second_number)
#             break
#         elif base_operator == "*":
#             print(first_number * second_number)
#             break
#
#     except ZeroDivisionError as error:
#         value += 1
#         print("Operation failed. Please enter right number! ZeroDivisionError")
#     except ValueError as error:
#         value += 1
#         print("Operation failed. Please enter right number! ValueError")
#     if value == 2:
#         print("Zero attempts left. GoodBye")