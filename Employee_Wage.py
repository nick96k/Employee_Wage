'''

    @Author : Nikhil Patil
    @Date : 22-08-24
    @Last Modified by : Nikhil Patil
    @Last Modified Date : 23-08-24
    @Title : Employee Wage Program


'''
import random

class EmployeeWage():

    #Constants
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    PART_TIME_DAY_HOUR = 4
    MONTH_DAYS = 20
    MAX_HOURS_PER_MONTH = 100


    @classmethod
    def check_attendance(self):
        """

            Description:
                Using random to check employee is present or not. If 0 then employee is absent, 1 for present and 2 for part time. 
            Parameter:
                None
            Return:
                Give choice 0, 1 or 2.

        """
        return random.choice([0, 1, 2])  


    @classmethod
    def calculate_daily_wage(self):
        """

            Description:
                Calculate Daily wages, wage per hour is 20 and full day hour is 8. 
            Parameter:
                None
            Return:
                Multiplication of wage per hour and full day hours.

        """
        return self.WAGE_PER_HOUR * self.FULL_DAY_HOUR


    @classmethod
    def part_time_employee_daily_wage(self):
        """

            Description:
                Calculate Daily wages for part time employee, wage per hour is 20 and haugh day hour is 4. 

            Parameter:
                None

            Return:
                Multiplication of part time day hours and wage per hour.

        """
        return self.PART_TIME_DAY_HOUR * self.WAGE_PER_HOUR 

    
    @classmethod
    def calculate_monthly_wage(self):
        """

            Description:
                Calculate monthly wages for the employees, for maximum hours in month is 100 and maximum day is 20.
            Parameter:
                None
            Return:
                total_days : Give Total working days in a month.
                total_hours : Give Total working hours in a month.

        """ 
        total_hours = 0
        total_days = 0

        while total_hours < self.MAX_HOURS_PER_MONTH and total_days < self.MONTH_DAYS  :
            attendance = self.check_attendance()
            if attendance == 1:
                total_hours += self.FULL_DAY_HOUR
            elif attendance == 2:
                total_hours += self.PART_TIME_DAY_HOUR
            else :
                total_hours += 0
            total_days +=1

        return total_days, total_hours


print("***Welcome to Employee Wage Computation Program***")
total_days, total_hours = EmployeeWage.calculate_monthly_wage()
print(f"Given Employee Total Present Days in Month : {total_days} ")
print(f"Given Employee Total Working Hours in Month : {total_hours} ")
print(f"Given Employee Total Wages for one Month  : {total_hours * EmployeeWage.MONTH_DAYS} ")


