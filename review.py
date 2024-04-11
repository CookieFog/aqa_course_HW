# Homework_7_1


# тут треба було написати свій мар це означає написати код котрий буде приймати ітеребл обьект
# та функцію котра буде виконувати код із всіма умовати

# example
#
# def custom_map(func, iterable_obj: list):
#     for item in iterable_obj:
#         yield func(item)
#
# def custom_map(func, iterable_obj: list):
#     res = []
#     for item in iterable_obj:
#         res.append(func(item))
#     return res


my_list = list(map(lambda x, y: x * y, [1, 2, 3], [4, 5, 6]))

print(my_list)

my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# тут теж саме як і у мар

# def custom_filter(func, iterable_obj: list):
#     for item in iterable_obj:
#         if func(item):
#            yield func(item)
#
# def custom_filter(func, iterable_obj: list):
#     res = []
#     for item in iterable_obj:
#         if func(item):
#             res.append(item)
#     return res

b = filter(lambda x: x % 2 == 0, my_list_2)
for x in b:
    print(x)


# Homework_7_2
# дуже багато зайвого коду
# трай зайвый
# та треба було приймати функцію як інпут від користуавча 
# def print_hi():
#     result = 'Hi'
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
#     
    
    
try:
    def DOD(x: int):
        return lambda y: pow(x, y)


    def test(arg):
        if callable(arg):
            print('start')
            print(arg(2))  # pow(x, y)
            print('finish')
        else:
            print("Hm, something went wrong!")

    test(DOD(10))
except:
    print("Error544")
