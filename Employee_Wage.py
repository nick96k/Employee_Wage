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
MONTH_DAYS = 20


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



def calculate_monthly_wage():

    """

        Description:
            Calculate monthly wages for the employees, wage per hour is 20, haugh day hour is 4 and monthly working days is 20. 

        Parameter:
            None

        Return:
            Multiplication of total monthly working hours and wage per hour.

    """
    
    total_daily_wage = []
    for _ in range(MONTH_DAYS):
        attendance = check_attendance()
        if attendance == 1:
            total_daily_wage.append(calculate_daily_wage())
            
        elif attendance == 2:
            total_daily_wage.append(part_time_employee_daily_wage())
        else :
            total_daily_wage.append(0)

    return sum(total_daily_wage), total_daily_wage


def main():
    print("***Welcome to Employee Wage Computation Program***")
    monthly_wage, day_wise_wage = calculate_monthly_wage()
    print(f"Given Employee monthly wages is : {monthly_wage}")
    print(f"Given Employee day wise monthly wages  : {day_wise_wage}")




if __name__ == "__main__":
    main()


