"""Recommend Cha Cha Cha"""
import math
def main(day):
    """Main Recommend Cha Cha Cha"""
    total_income = 0
    hourly_wage = 8720
    for _ in range(day):
        hourly_worked = float(input())
        rounded_hours = math.ceil(hourly_worked)
        daily_income = rounded_hours * hourly_wage
        total_income += daily_income
    print(total_income)
main(int(input()))
