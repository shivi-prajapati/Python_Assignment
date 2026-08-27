# Exercise 1: Leap Year Checker
# Write a program that takes a year as input from the user and checks whether it is a leap year or not.

def leap_year():
    x=int(input("Enter a Year :"))
    if x%400==0 or x%4==0 and x%100!=0 :
        print(f'{x} is a leap year')
    else:
        print(f'{x} is not a leap year')
leap_year()



# Exercise 2: Fibonacci Sequence Generator
# Write a Python script to print the first N terms of the Fibonacci sequence, where N is provided by the user.

def fib():
    num=int(input('Enter a number :'))
    prev=0
    curr=1
    print(f"{prev} {curr}",end=' ')
    for i in range(1,num):
        sum=prev + curr
        prev=curr
        curr=sum
        print(sum,sep=',',end=' ')
fib()
        

# Exercise 3: Prime Number Checker
# Write a program that checks whether a positive integer entered by the user is a prime number.

def prime_no():
    num=int(input('Enter a positive number :'))
    if num<=0 or num==1:
        return 0
    digit=num//2
    for i in range(2,digit+1):
        if num%i==0:
            print(' is not a Prime Number')
            break
    else:
        print('is a prime number')       
prime_no()


# Exercise 4: Odd or Even Checker
# Write a program that prompts the user for an integer and prints whether it is even or odd.

def even_odd():
    num=int(input("Enter a Number :"))
    if num%2==0:
        print(f'{num} is an Even Number')
    else:
        print(f'{num} is a Odd Number')
even_odd()


# Exercise 5: Basic Operator Calculator
# Create a program that takes two numbers and a math operator (+, -, *, /) from the user, performs the corresponding calculation, and 
# prints the result.

def calci():
    num1=int(input('Enter first Number :'))
    num2=int(input('Enter second Number :'))
    op=input('Choose a math operator :')
    if op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='*':
        print(num1*num2)
    elif op=="/":
        print(num1/num2)
    else:
        print('Invalid Operator')
calci()


# Exercise 6: Sum of N Natural Numbers
# Write a script that accepts a positive integer N from the user and calculates the sum of all natural numbers up to N.
def sum():
    num=int(input("Enter a Positive Integer :"))
    result=1
    for i in range(1,num+1):
        result=i*(i+1)/2
    print(f'Sum of {num} natural number is {result}')
sum()


# Exercise 7: Multiplication Table Generator
# Write a program that takes an integer from the user and prints its multiplication table from 1 to 10.

def table():
    num=int(input("Enter an Integer :"))
    for i in range(1,11):
        result=num*i
        print('{0}*{1}={2}'.format(num,i,result))
table()

# Exercise 8: Score to Grade Converter
# Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

def score():
    num=int(input('Enter Your Score :'))
    if 90<=num<=100:
        print('Your Grade is : A')
    elif 80<=num<=89:
        print('Your Grade is : B')
    elif 70<=num<=79:
        print('Your Grade is : C')
    elif 60<=num<=69:
        print('Your Grade is : D')
    else :
        print('Your Grade is : F')
score()