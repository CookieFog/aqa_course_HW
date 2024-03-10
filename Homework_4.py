# Homework task #1 date 07.03.2024------------------------------------------------------------------------
list_1 = ["john", "marta", "james", "amanda", "marianna"]
list_2 = []
Name_john = list_1.pop(list_1.index("john",))
Name_marta = list_1.pop(list_1.index("marta"))
Name_james = list_1.pop(list_1.index("james"))
Name_amanda = list_1.pop(list_1.index("amanda"))
Name_marianna = list_1.pop(list_1.index("marianna"))

list_2.append(Name_john.capitalize())
list_2.append(Name_marta.capitalize())
list_2.append(Name_james.capitalize())
list_2.append(Name_amanda.capitalize())
list_2.append(Name_marianna.capitalize())
print(list_2)
# Homework task #2 date 07.03.2024------------------------------------------------------------------------
list_3 = ["FirstItem", "FriendsList", "MyTuple"]

list_3[1] = "Friends_list"
list_3[0] = "First_item"
list_3[2] = "My_Tuple"
print(list_3)
# Homework task #3 date 07.03.2024------------------------------------------------------------------------
dictionary_1 = {'PHP': 'PHP creator is Rasmus Lerdorf', 'Python': 'Python creator isGuido van Rossum',
'C++': 'C++ creator is Björn Stroustrup', 'C#': 'C# creator isDennis Ritchie'
                }
if 'PHP' and 'Python' and 'C++' and 'C#' in dictionary_1:
    print(dictionary_1.get('PHP'),". NO it isn't!")
    print("My favorite programming language is Python. It was created by Guido van Rossum.")
    print(dictionary_1.get('Python'),". Yes this is it:)")
    print(dictionary_1.get('C++'), ". NO it isn't!")
    print("My favorite programming language is Python. It was created by Guido van Rossum.")
    print(dictionary_1.get('C#'), ". NO it isn't!")
    print("My favorite programming language is Python. It was created by Guido van Rossum.")

del dictionary_1['PHP']
print(dictionary_1)
# Homework task #4 date 07.03.2024-------------------------------------------------------------------------
names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
for names in ['Jack', 'Leon', 'Alice', 'Bob']:
    print(names)
    continue
# Homework task #5 date 09.03.2024-------------------------------------------------------------------------
types = [1, 10, 2, 12, {'key': 'value'}]    # Please choose any value in field {'key': 'value'} example 544
for value in types:
    if (isinstance(types[0], int) and isinstance(types[1], int)
            and isinstance(types[2], int) and isinstance(types[3], int) and isinstance(types[4], int)):
        print("True")
        print(value)
        continue
    else:
        print("loop 'For' is not working with float. This program working only with int! ")
        print("!unexpected error loop is closed!")
    break
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
value = 0
while value < 2:
    print("Welcome to calculator version 2.1. Warning you have only 2 attempts and after that program will close!")
    first_number = float(input("Please choose first number"))
    base_operator = input("Please choose operator")
    second_number = float(input("Please choose second number"))
    if base_operator == "+":
        print(first_number + second_number)
        break
    elif base_operator == "-":
        print(first_number - second_number)
        break
    if second_number == 0:
        value += 1
        if value == 2:
            print("You choose wrong value.Program is closed")
    elif base_operator == "/":
        print(first_number / second_number)
        break
    elif base_operator == "*":
        print(first_number * second_number)
        break

