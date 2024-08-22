'''

    @Author : Nikhil Patil
    @Date : 22-08-24
    @Last Modified by : Nikhil Patil
    @Last Modified Date : 22-08-24
    @Title : Employee Wage Program


'''

import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_DAY_HOUR = 4


def check_attendance():

    """

        Description:
            Using random to check employee is present or not. If 0 then employee is absent, 1 for present and 2 for part time. 

        Parameter:
            None

        Return:
            Give choice 0, 1 or 2.

    """

    return random.choice([0, 1, 2])  


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


def part_time_employee_daily_wage():

    """

        Description:
            Calculate Daily wages for part time employee, wage per hour is 20 and haugh day hour is 4. 

        Parameter:
            None

        Return:
            Multiplication of part time day hours and wage per hour.

    """
    return PART_TIME_DAY_HOUR * WAGE_PER_HOUR


def main():
    print("***Welcome to Employee Wage Computation Program***")
    attendance = check_attendance()

    match (attendance):
        case 1:
            print(f"Given Employee is Full time Employee.... \nThere daily wage : {calculate_daily_wage()}")
        case 2:
            print(f"Given Employee is Part time Employee.... \nThere daily wage : {part_time_employee_daily_wage()}")
        case _ :
            print(f"Given Employee is Absent.... \nThere daily wage : {0}")


if __name__ == "__main__":
    main()


