''' ______ '''

import calendar
from datetime import date


#Takes custom date and returns it.
def main():
    #Prompts the user to enter a year and stores it's value.
    print("Enter a year.")
    year = int(input(">"))

    #Prompts the user to enter a month and stores it's value.
    print("\nPlease select a month.")
    print('''1 - Jan
2 - Feb
3 - Mar
4 - Apr
5 - May
6 - Jun
7 - Jul
8 - Aug
9 - Sep
10 - Oct
11 - Nov
12 - Dec''')
    while True:     #To make sure the user gives an input within the given range.
        month = int(input(">"))
        if 0 < month <= 12:
            break

    #Prompts the user to enter a day of the month and stores it's value.
    print("\nEnter a given day of the month.")
    day = validate_days(year, month)

    return str(calendar.month_name[month]) + " " + str(day) + "," + str(year)


#This function is used to validate the number of days in that month.
def validate_days(year, month):
    month_range = calendar.monthrange(year, month)
    res = int(''.join(map(str, month_range))) 
    mod = res % 100
    print("Day should be in the range of 0 to",mod)
    while True:
        day = int(input(">"))
        if 0 <= day <= mod:
            break
    return day

