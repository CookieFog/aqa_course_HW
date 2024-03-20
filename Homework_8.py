# Homework_8_1
import os
import csv

try:

    with open('C:/Users/user/Desktop/test_file.csv', mode='w') as file:
        value = 0
        currency = 39.16
        salary_1 = 1000  # $
        salary_2 = 1200  # $
        salary_3 = 1500  # $

        Sum_1 = salary_1 * currency
        Sum_2 = salary_2 * currency
        Sum_3 = salary_3 * currency
        file.writelines('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec\n')

        file.write("Employee1\n")
        if Sum_1 >= 39160:
            while value < 12:
                file.write('39160,')
                value += 1

        file.write("\nEmployee2\n")

        if Sum_2 >= 46991:
            while value < 24:
                file.write('46992,')
                value += 1
            file.write("\nEmployee3\n")
        if Sum_3 >= 58739:
            while value < 36:
                file.write('58739,')
                value += 1

except:
    print("HMM,something went wrong!")

with os.mkdir('C:/Users/user/Desktop/salaries_uah.csv'):
    file.write('hi')
