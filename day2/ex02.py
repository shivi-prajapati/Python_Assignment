'''Exercise 2: Reversed Uppercased String
Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, 
and prints the result.'''

def reverse():
    string=input('Enter a String :')
    new_str=string[::-1]
    print(new_str.upper())
reverse()

