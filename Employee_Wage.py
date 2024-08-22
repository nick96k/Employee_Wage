'''

    @Author: Nikhil Patil
    @Date: 22-08-24
    @Last Modified by: Nikhil Patil
    @Last Modified time: 22-08-24
    @Title : Employee Wage Program


'''

import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

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


def calculate_daily_wage():

    """

        Description:
            Calculate Daily wages, wage per hour is 20 and full day hour is 8. 

        Parameter:
            None

        Return:
            Multiplication of wage per hour and full day hours.


    """

    return WAGE_PER_HOUR * FULL_DAY_HOUR



def main():
    print("***Welcome to Employee Wage Computation Program***")
    attendance = check_attendance()
    if attendance == 1:
        print(f"Your daily wages is {calculate_daily_wage()}.")
    else:
        print("Employee is Absent")


if __name__ == "__main__":
    main()


