'''

    @Author : Nikhil Patil
    @Date : 22-08-24
    @Last Modified by : Nikhil Patil
    @Last Modified Date : 26-08-24
    @Title : Employee Wage Program


'''
import random

class EmployeeWage:
    def __init__(self):
        """
        
            Description: 
                Dictionary to store total wages for all companies
            Parameters:
                None
            Return:
                None

        """
        self.company_wages = {}


    @classmethod
    def check_attendance(cls):
        """
            Description:
                Using random to check employee is present or not. If 0 then employee is absent, 1 for present, and 2 for part-time.
            Parameters:
                None
            Return:
                None


        """
        return random.choice([0, 1, 2])


    @classmethod
    def calculate_daily_wage(cls, wage_per_hour, full_day_hour):
        """
            
            Description:
                Calculate daily wages based on wage per hour and full day hours.
            Parameters:
                wage_per_hour (int): Wage per hour.
                full_day_hour (int): Working hours for full day employee.
            Return:
                Multiplication of wage per hour and full day hour.


        """
        return wage_per_hour * full_day_hour


    @classmethod
    def part_time_employee_daily_wage(cls, wage_per_hour, part_time_day_hour):
        """
            
            Description:
                Calculate daily wages for part-time employees based on wage per hour and part-time day hours.
            Parameters:
                wage_per_hour (int): Wage per hour.
                part_time_day_hour (int): Working hours for part time employee.
            Return:
                Multiplication of wage per hour and part time day hour.


        """
        return wage_per_hour * part_time_day_hour


    def calculate_monthly_wage(self, company_name, wage_per_hour, full_day_hour, part_time_day_hour, max_working_days, max_working_hours):
        """
            
            Description:
                Calculates total wage, total hours, and total days for a specific company and stores it in the dictionary.
            Parameters:
                company_name (str): The name of the company.
                wage_per_hour (int): The wage per hour for the employee.
                full_day_hour (int): The number of hours for a full day of work.
                part_time_day_hour (int): The number of hours for a part-time day of work.
                max_working_days (int): The maximum number of working days in the month.
                max_working_hours (int): The maximum number of working hours in the month.
            Return:
                None
        
        """
        total_hours = 0
        total_days = 0
        total_wage = 0

        while total_hours < max_working_hours and total_days < max_working_days:
            attendance = self.check_attendance()
            if attendance == 1:
                total_hours += full_day_hour
                total_wage += self.calculate_daily_wage(wage_per_hour, full_day_hour)
            elif attendance == 2:
                total_hours += part_time_day_hour
                total_wage += self.part_time_employee_daily_wage(wage_per_hour, part_time_day_hour)
            total_days += 1

        # Store the total wage for the company in the dictionary
        self.company_wages[company_name] = total_wage


    def display_company_wages(self):
        """
            
            Description:
                Displays the total wages for all companies.
            Parameters:
                None
            Return:
                None    

        """
        print("\nTotal Wages for all Companies:")
        for company_name, total_wage in self.company_wages.items():
            print(f"Total Wage for {company_name} : {total_wage}")


def main():
    print("\n*** Welcome to Employee Wage Computation Program ***")
    
    employee_wage = EmployeeWage()

    multiple_companies = {
        "Infostrech": {"wage_per_hour": 30, "full_day_hour": 6, "part_time_day_hour": 3, "max_working_days": 18, "max_working_hours": 90},
        "Wipro": {"wage_per_hour": 25, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 22, "max_working_hours": 120},
        "Tech M": {"wage_per_hour": 20, "full_day_hour": 9, "part_time_day_hour": 5, "max_working_days": 24, "max_working_hours": 110},
        "TCS": {"wage_per_hour": 20, "full_day_hour": 8, "part_time_day_hour": 5, "max_working_days": 24, "max_working_hours": 105},
        "Accenture": {"wage_per_hour": 25, "full_day_hour": 9, "part_time_day_hour": 5, "max_working_days": 22, "max_working_hours": 100},
    }

    for company_name, values in multiple_companies.items():
        employee_wage.calculate_monthly_wage(
            company_name,
            values["wage_per_hour"],
            values["full_day_hour"],
            values["part_time_day_hour"],
            values["max_working_days"],
            values["max_working_hours"]
        )

    employee_wage.display_company_wages()


if __name__ == "__main__":
    main()
