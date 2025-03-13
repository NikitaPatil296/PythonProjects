
DaysInMonths = [0,31,28,30,31,30,31,30,31,30,31,30,31]

def is_leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 != 0)

def day_In_Months(year,month):
    if 12 <= month <= 1:
        return 'Invalid month'
    elif month == 2 and is_leapYear(year):
        return 29
    else:
        return DaysInMonths(month)
        
print(is_leapYear(2024))
print("Days in months =",day_In_Months(2024,2))