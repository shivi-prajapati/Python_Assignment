'''Exercise 4: Odd or Even Checker
Write a program that prompts the user for an integer and prints whether it is even or odd.'''

def even_odd():
    num=int(input("Enter a Number :"))
    if num%2==0:
        print(f'{num} is an Even Number')
    else:
        print(f'{num} is a Odd Number')
even_odd()