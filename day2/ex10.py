'''Exercise 10: Run-Length String Compression
Write a program that prompts the user to enter a text string and compresses it using run-length encoding (listing character counts next to each repeated character). If the compressed string is not smaller in size than the original string, print the original string.

Sample Input: "aabcccccaaa"
Sample Output: "a2b1c5a3"
Sample Input: "abcd"
Sample Output: "abcd" (since "a1b1c1d1" is longer than "abcd")'''

def string_comp():
    str=input('Enter a Text :')
    count=1
    i=0
    j=1
    while j<len(str):
        if str[i]==str[j]:
            count +=1
        else:
            print(str[i],count,sep='',end='')
            i=j
            count=1
        j+=1
    print(str[i],count,sep='',end='')
string_comp()

