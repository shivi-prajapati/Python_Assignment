'''Exercise 4: Vowel & Consonant Frequency Write a program that prompts the user to enter a string and counts:
The individual frequency of each vowel (a, e, i, o, u), case-insensitively.The total count of all consonants.'''

def frequency():
    str=input("Enter a String :")
    str1=str.lower()
    count=0
    print("Frequency of a=",str1.count('a'))
    print("Frequency of e=",str1.count('e'))
    print("Frequency of i=",str1.count('i'))
    print("Frequency of o=",str1.count('o'))
    print("Frequency of u=",str1.count('u'))
    for i in str1:
        if i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i==' ':
            continue
        else:
            count +=1
    print('Total consonants=',count)
frequency()