'''Exercise 2: Fibonacci Sequence Generator
Write a Python script to print the first N terms of the Fibonacci sequence, where N is provided by the user.'''

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