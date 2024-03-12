# Homework task #1 date 07.03.2024------------------------------------------------------------------------
list_1 = ["john", "marta", "james", "amanda", "marianna"]

for names in list_1:
    print(names.capitalize())
# Homework task #2 date 07.03.2024------------------------------------------------------------------------
list_3 = ["FirstItem", "FriendsList", "MyTuple"]
result_list = []
for element in list_3:
    result_str = ''
    for letter in element:
        if letter.isupper() and result_str:
            result_str += f'_{letter.lower()}'
        else:
            result_str += letter.lower()

    result_list.append(result_str)

print(result_list)

# Homework task #3 date 07.03.2024------------------------------------------------------------------------
dictionary_1 = {'PHP': 'PHP creator is Rasmus Lerdorf', 'Python': 'Python creator isGuido van Rossum',
'C++': 'C++ creator is Björn Stroustrup', 'C#': 'C# creator isDennis Ritchie'
                }
for name, creator in dictionary_1.items():
    print(f"My favorite programming language is {name}. It was created by {creator}")
del dictionary_1['PHP']
print(dictionary_1)
# Homework task #4 date 07.03.2024-------------------------------------------------------------------------
list_4 = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
for item in list_4:
    if isinstance(item, str):
        print(item)
# Homework task #5 date 09.03.2024-------------------------------------------------------------------------
types = [1, 10, 2, 12, {'key': 'value'}]    # Please choose any value in field {'key': 'value'} example 544
for value in types:
    if isinstance(value, int):

        print(value)
        continue
    else:
        print("loop 'For' is not working with float. This program working only with int! ")
        print("!unexpected error loop is closed!")
    break
# Homework task #6 date 09.03.2024---------------------------------------------------------------------------
dict_1 = input("awaiting letter")
dict_result = {}
for x in dict_1: x: 'f'

dict_result[x] = dict_result.get(x, 0) + 1
''.join([f'{key},{value}' for key, value in dict_result.items()])
print(dict_result)

# # Homework task #7 date 10.03.2024----------------------------------------------------------------------------
value = 0
while value < 2:
    try:
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
        elif base_operator == "/":
            print(first_number / second_number)
            break
        elif base_operator == "*":
            print(first_number * second_number)
            break

    except ZeroDivisionError as error:
        value += 1
        print("Operation failed. Please enter right number! ZeroDivisionError")
    except ValueError as error:
        value += 1
        print("Operation failed. Please enter right number! ValueError")
    if value == 2:
        print("Zero attempts left. GoodBye")