# Homework_7_1

my_list = list(map(lambda x, y: x * y, [1, 2, 3], [4, 5, 6]))

print(my_list)

my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = filter(lambda x: x % 2 == 0, my_list_2)
for x in b:
    print(x)

# Homework_7_2










#Homework_7_3

def print_hi():
    print("Hi")

def print_bye():
    print("Bye")

def evaluate():
    user_input = input("Please enter print_hi() or print_bye()")
    eval(user_input)
evaluate()