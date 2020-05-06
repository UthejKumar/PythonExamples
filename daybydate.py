''' "Day By Date" ~ by Uthej Kumar
    This program will take a given date as input.
    It will provide you which day of the week falls on that date.'''

import calendar

print("*"*15,"Day By Date Simulator","*"*15,"\n")


#This function calculates the day of the week.
def find_day(year, month, day):
    day_val = calendar.weekday(year, month, day)
    day_name = weekday_name(day_val)
    print("\nThe given day of week for that date is",day_name)


#This function takes day of week value in int and gives corresponding string value.
#It will be much easier for the user to understand.
def weekday_name(day_val):
    if day_val == 0:
        day_name = "Monday"
        return day_name
    elif day_val == 1:
        day_name = "Tuesday"
        return day_name
    elif day_val == 2:
        day_name = "Wednesday"
        return day_name
    elif day_val == 3:
        day_name = "Thursday"
        return day_name
    elif day_val == 4:
        day_name = "Friday"
        return day_name
    elif day_val == 5:
        day_name = "Saturday"
        return day_name
    elif day_val == 6:
        day_name = "Sunday"
        return day_name


#This function is used to validate the the user's input for days.
#Checks if the input is within the corresponding range for that month.
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
day = validate_days(year, month)    #Validate the no. of days in a month.


#Passing the given user input values to "find_day" function.
find_day(year, month, day)
