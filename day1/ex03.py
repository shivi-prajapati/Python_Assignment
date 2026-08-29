'''Exercise 3: Prime Number Checker
Write a program that checks whether a positive integer entered by the user is a prime number.'''

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