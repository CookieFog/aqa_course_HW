# Homework_10_1
import time


# def decorator(func):
#     def inner(*args):
#         start = time.time()
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


# def logger(func):
#     def inner(*args):
#         start = time.time()
#         print(f'Function {func.__name__} starting working now. This func will sum 2 ints ')
#         func(*args)
#         end = time.time()
#         print(f'Function {func.__name__} took {end - start} time')
#
#     return inner
#
#
# @logger("Plus action")
# def plus(x, y):
#     time.sleep(2)
#
#     return x + y
#
#
# plus(10, 20)
#


# def logger(func):
#     def wrapper(*arg, **kwargs):
#         reslut = func(*arg, **kwargs)
#         print(f'This function {func.__name__} will sum 2 ints ')
#         time.sleep(1)
#         return reslut
#
#     return wrapper
#
#
# @logger
# def plus(x, y):
#     return x + y
#
#
# plus(10, 20)


def logger(text):
    def sub_logger_decorator(func):
        def wrap(*args, **kwargs):
            print(f' {text} {args}')
            result = func(*args, **kwargs)
            return result

        return wrap

    return sub_logger_decorator


@logger('Sum 2 arguments')
def plus(x, y):
    time.sleep(1)
    return x + y


plus(10, 20)
print(plus(10, 20))
