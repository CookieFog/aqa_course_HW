import os

# try:
#
#     file_path = open('C:/Users/user/Desktop/test_file.csv', mode='w')
#     # file_path.writelines(' Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec\n')
#     # file_path.write('Employee_1\n')
#     # file_path.write('39 157,39 157,39 157,39 157,39 157,39 157,39 157,39 157,39 157,39 157,39 157,39 157')
#     currency = 39.16
#     salary_1 = 1000  # $
#     salary_2 = 1200  # $
#     salary_3 = 1500  # $
#
#     Sum_1 = salary_1 * currency
#     Sum_2 = salary_2 * currency
#     Sum_3 = salary_3 * currency
#
#     if file_path == Sum_1:
#         file_path.write('39 160')
#
#     file_path.close()
# except:
#     print("HMM,something went wrong!")


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
        # file.writelines(' Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec')
        file.write("Employee1\n")
        if Sum_1 >= 39160:
            while value < 12:

                file.write('    39160\n')
                value += 1
        file.write("    Employee2\n")

        if Sum_2 >= 46991:
            while value < 24:

                file.write('46992\n')
                value += 1
            file.write("Employee3\n")
        if Sum_3 >= 58739:
            while value < 36:
                file.write('58739\n')
                value += 1

except:
    print("HMM,something went wrong!")
