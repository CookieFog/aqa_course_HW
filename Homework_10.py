# Homework_10_1
import time


# def decorator(func):
#     def inner(*args):
#         start = time.time()
#         print(f'Function {func.__name__} starting working')
#         func(*args)
#         end = time.time()
#         print(f'Function {func.__name__} took {end - start} time')
#
#     return inner
#
#
# @decorator
# def sum_1(a, b):
#     time.sleep(1)
#     print(a + b)
#
#
# sum_1(4, 5)

# Homework_10_2


def logger(func):
    def inner(*args):
        start = time.time()
        print(f'Function {func.__name__} starting working now. This func will sum 2 ints ')
        func(*args)
        end = time.time()
        print(f'Function {func.__name__} took {end - start} time')

    return inner


@logger
def plus(x, y):
    time.sleep(2)
    print(x + y)
    return x + y


plus(10, 20)
