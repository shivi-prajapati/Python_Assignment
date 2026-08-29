'''Exercise 7: Multiplication Table Generator
Write a program that takes an integer from the user and prints its multiplication table from 1 to 10.'''

def table():
    num=int(input("Enter an Integer :"))
    for i in range(1,11):
        result=num*i
        print('{0}*{1}={2}'.format(num,i,result))
table()