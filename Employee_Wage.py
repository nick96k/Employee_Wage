'''

    @Author : Nikhil Patil
    @Date : 22-08-24
    @Last Modified by : Nikhil Patil
    @Last Modified Date : 26-08-24
    @Title : Employee Wage Program


'''
import random

class EmployeeWage():

    @classmethod
    def check_attendance(cls):
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
    def calculate_daily_wage(cls, wage_per_hour, full_day_hour):
        """

            Description:
                Calculate Daily wages, wage per hour is 20 and full day hour is 8. 
            Parameter:
                wage_per_hour (int): The wage per hour for the employee.
                full_day_hour (int): The number of hours for a full day of work.
            Return:
                Multiplication of wage per hour and full day hours.

        """
        return wage_per_hour * full_day_hour


    @classmethod
    def part_time_employee_daily_wage(cls, wage_per_hour, part_time_day_hour):
        """

            Description:
                Calculate Daily wages for part time employee, wage per hour is 20 and haugh day hour is 4. 
            Parameter:
                wage_per_hour (int): The wage per hour for the employee.
                part_time_day_hour (int): The number of hours for a part-time day of work.
            Return:
                Multiplication of part time day hours and wage per hour.

        """
        return wage_per_hour * part_time_day_hour 

    
    @classmethod
    def calculate_monthly_wage_for_multiple_companies(cls, wage_per_hour, full_day_hour, part_time_day_hour, max_working_days, max_working_hours):
        """

            Description:
                Calculates the total wage, total hours, total days, and daily wages for the month for a specific company.
            Parameters:
                wage_per_hour (int): The wage per hour for the employee.
                full_day_hour (int): The number of hours for a full day of work.
                part_time_day_hour (int): The number of hours for a part-time day of work.
                max_working_days (int): The maximum number of working days in the month.
                max_working_hours (int): The maximum number of working hours in the month.
            Return:
                total_days : Total working days in a month.
                total_hours : Total working hours in a month.
                total_wage : Total wage earned in the month.        

        """ 
        total_hours = 0
        total_days = 0
        total_wage =0

        while total_hours < max_working_hours and total_days < max_working_days  :
            attendance = cls.check_attendance()
            if attendance == 1:
                total_hours += full_day_hour
                total_wage += cls.calculate_daily_wage(wage_per_hour, full_day_hour)
            elif attendance == 2:
                total_hours += part_time_day_hour
                total_wage += cls.part_time_employee_daily_wage(wage_per_hour, part_time_day_hour)
            # If absent (attendance == 0), no hours or wage is added
            total_days += 1

        return total_days, total_hours, total_wage
    

def main():
    print("\n*** Welcome to Employee Wage Computation Program ***")

    multiple_companies = {
        "Infostrech": {"wage_per_hour": 30, "full_day_hour": 6, "part_time_day_hour": 3, "max_working_days": 18, "max_working_hours": 90},
        "Wipro": {"wage_per_hour": 25, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 22, "max_working_hours": 120},
        "Tech M": {"wage_per_hour": 20, "full_day_hour": 9, "part_time_day_hour": 5, "max_working_days": 24, "max_working_hours": 110},
        "TCS": {"wage_per_hour": 20, "full_day_hour": 8, "part_time_day_hour": 5, "max_working_days": 24, "max_working_hours": 105},
        "Accenture": {"wage_per_hour": 25, "full_day_hour": 9, "part_time_day_hour": 5, "max_working_days": 22, "max_working_hours": 100},
    }

    for company_name, values in multiple_companies.items():
        print(f"\n\t** Monthly Wages for {company_name} **")
        total_days, total_hours, total_wage = EmployeeWage.calculate_monthly_wage_for_multiple_companies(
            values["wage_per_hour"],
            values["full_day_hour"],
            values["part_time_day_hour"],
            values["max_working_days"],
            values["max_working_hours"]
        )

        print(f"Employee Total Present Days in the Month: {total_days}")
        print(f"Employee Total Working Hours in the Month: {total_hours}")
        print(f"Employee Total Wages for the Month: {total_wage}")


if __name__ == "__main__":
    main()