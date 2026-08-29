'''Exercise 12: Date Validator & Pretty Formatter
Write a program that prompts the user to enter a date string in the format "DD/MM/YYYY"'''

date = input("Enter date (DD/MM/YYYY): ")
day, month, year = date.split("/")
day = int(day)
month = int(month)
year = int(year)
months = ("January","February","March","April","May","June","July","August","September","October","November","December")
if month < 1 or month > 12:
    print("Invalid Date")

else:
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_days = 31

    elif month in (4, 6, 9, 11):
        max_days = 30

    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28

    if day < 1 or day > max_days:
        print("Invalid Date")
    else:
        print(f"{months[month - 1]} {day}, {year}")
