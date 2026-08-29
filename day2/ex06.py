'''Exercise 6: Shift Cipher Encrypter Write a program that prompts the user for a text string and a shift integer, 
and encrypts the text using a Caesar cipher. It should shift each alphabetical character in the string by the 
specified shift number down the alphabet. Maintain uppercase and lowercase characters, and leave spaces or 
punctuation marks completely unchanged.'''

def shift():
    x=input('Enter a Text :')
    y=int(input('Shift by :'))
    result=''
    for char in x:
        if char.isupper():
            result += chr((ord(char)-65 + y)%26+65)
        elif char.islower():
            result += chr((ord(char)-97+y)%26+97)
        else:
            result += char
    print(result)
shift()