'''Exercise 1: Leap Year Checker
Write a program that takes a year as input from the user and checks whether it is a leap year or not.'''

def leap_year():
    x=int(input("Enter a Year :"))
    if x%400==0 or x%4==0 and x%100!=0 :
        print(f'{x} is a leap year')
    else:
        print(f'{x} is not a leap year')
leap_year()
