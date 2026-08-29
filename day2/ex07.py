'''Exercise 7: Manual Substring Counter
Write a program that prompts the user to enter a main text string and a substring. 
Count how many times the substring appears in the main string without using Python's built-in .count() method.'''

def sub_str():
    string=input('Enter a String :')
    target=input('Enter a Substring :')
    y=len(target)
    count=0
    for i in range(0,len(string)+1):
        if string[i:i+y]==target:
            count += 1
    print(count)
sub_str()