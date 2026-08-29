'''Exercise 8: Score to Grade Converter
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:'''

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