# Homework_8_1
import os
import csv

#
# try:
#
#     with open('C:/Users/user/Desktop/test_file.csv', mode='w') as file:
#         value = 0
#         currency = 39.16
#         salary_1 = 1000  # $
#         salary_2 = 1200  # $
#         salary_3 = 1500  # $
#
#         Sum_1 = salary_1 * currency
#         Sum_2 = salary_2 * currency
#         Sum_3 = salary_3 * currency
#         file.writelines('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec\n')
#
#         file.write("Employee1\n")
#         if Sum_1 >= 39160:
#             while value < 12:
#                 file.write('39160,')
#                 value += 1
#
#         file.write("\nEmployee2\n")
#
#         if Sum_2 >= 46991:
#             while value < 24:
#                 file.write('46992,')
#                 value += 1
#             file.write("\nEmployee3\n")
#         if Sum_3 >= 58739:
#             while value < 36:
#                 file.write('58739,')
#                 value += 1
#
# except:
#     print("HMM,something went wrong!")
#
# with os.mkdir('C:/Users/user/Desktop/salaries_uah.csv'):
#     file.write('hi')

__file__ = open('C:/Users/user/Desktop/test_file.csv', mode='r')

try:
    with open('C:/Users/user/Desktop/test_file.csv', mode='r') as __file__:
        # path = os.path.dirname('__file__')
        print(__file__)
        print(__file__.readlines())
    currency = 39.16
    salary_1 = 1000  # $
    salary_2 = 1200  # $
    salary_3 = 1500  # $
    Sum_1 = salary_1 * currency
    Sum_2 = salary_2 * currency
    Sum_3 = salary_3 * currency
    list_1 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',  'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    list_2 = ['Employee1', int(Sum_1), int(Sum_1), int(Sum_1), int(Sum_1), int(Sum_1), int(Sum_1),int(Sum_1),
              int(Sum_1), int(Sum_1), int(Sum_1), int(Sum_1), int(Sum_1)]

    list_3 = ['Employee2', int(Sum_2), int(Sum_2), int(Sum_2), int(Sum_2), int(Sum_2), int(Sum_2), int(Sum_2),
              int(Sum_2), int(Sum_2), int(Sum_2), int(Sum_2), int(Sum_2)]

    list_4 = ['Employee3', int(Sum_3), int(Sum_3), int(Sum_3), int(Sum_3), int(Sum_3), int(Sum_3), int(Sum_3),
              int(Sum_3), int(Sum_3), int(Sum_3), int(Sum_3), int(Sum_3)]
    print(list_2)
    print(list_3)
    print(list_4)

    with open('salaries_uah.csv', mode='w') as file:
        print('ok')

        file.write('Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec\n')
        file.write('Employee1, 39160, 39160, 39160, 39160, 39160, 39160, 39160, 39160, 39160, 39160, 39160, 39160\n')
        file.write('Employee2, 46991, 46991, 46991, 46991, 46991, 46991, 46991, 46991, 46991, 46991, 46991, 46991\n')
        file.write('Employee3, 58739, 58739, 58739, 58739, 58739, 58739, 58739, 58739, 58739, 58739, 58739, 58739\n')

except:
    print("Hm,  something go wrong error!")

# path = os.path.dirname("C:/Users/user/Desktop/test_file.csv'")
#
# result_path = os.path.join(path, 'test_file.csv')
#
# with open(result_path, mode="r") as file:
#     print("ok")
#
# print(result_path.readlines())
#
# # 'str' object has no attribute 'readlines'
