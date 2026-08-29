'''Exercise 8: Write a program that prompts the user to enter a full name (first name, middle name, last name)
and anonymizes it. The output should print the initials of the first and middle names followed by
the full last name. If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"'''

def title_naming():
    string=input('Enter a Name:')
    string=string.split()
    for i in string:
        if i!=string[-1]:
            print(i[0].upper()+".",end=' ')
        else:
            print(i[0].upper()+i[1:].lower())
title_naming()