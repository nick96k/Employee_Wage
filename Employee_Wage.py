'''

    @Author: Nikhil Patil
    @Date: 22-08-24
    @Last Modified by: Nikhil Patil
    @Last Modified time: 22-08-24
    @Title : Employee Wage Program


'''

import random

def check_attendance():

    """

        Description:
            Using randome to check employee is present or not. If 0 then employee is absent, 1 for present. 

        Parameter:
            None

        Return:
            Give choice 0 or 1.


    """

    return random.choice([0, 1])  


def main():
    print("Welcome to Employee Wage Computation Program")
    attendance = check_attendance()
    if attendance == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")
        

if __name__ == "__main__":
    main()
