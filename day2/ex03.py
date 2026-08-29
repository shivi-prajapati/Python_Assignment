'''Exercise 3: Email Domain Extractor
Write a program that prompts the user to enter an email address string. Extract the domain name 
(the part after the @) and print it. If the string is not a valid email (does not contain exactly one @), print "Invalid Email".'''

def email():
    email_str=input("Enter Your Email :")
    for i in email_str:
        if i=='@':
            continue
        print(i,end='')
email()