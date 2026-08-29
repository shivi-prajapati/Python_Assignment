'''Exercise 5: Custom Title Case Formatter Write a program that accepts a string input from the user and outputs it in Title Case 
(capitalizing the first letter of each word and lowercasing the remaining letters). Do not use Python's built-in .title() method.'''

def title():
    string=input('Enter a String :')
    for i in string.split():
        print(i[0].upper()+i[1:].lower(),end=' ')
title()