'''Exercise 6: Sum of N Natural Numbers
Write a script that accepts a positive integer N from the user and calculates the sum of all natural numbers up to N.'''


def sum():
    num=int(input("Enter a Positive Integer :"))
    result=1
    for i in range(1,num+1):
        result=i*(i+1)/2
    print(f'Sum of {num} natural number is {result}')
sum()