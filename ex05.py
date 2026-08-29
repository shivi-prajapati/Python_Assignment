'''Exercise 5: Basic Operator Calculator
Create a program that takes two numbers and a math operator (+, -, *, /) from the user, performs the corresponding calculation, and 
prints the result.'''

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