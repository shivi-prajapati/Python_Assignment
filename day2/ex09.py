'''Exercise 9: Longest Palindromic Substring
Write a program that prompts the user to enter a text string and finds the longest substring within 
it that reads the same forward and backward. If there are multiple palindromic substrings of the same maximum length, 
print any one of them.

Sample Input: babad""
Sample Output: "bab" (or "aba")
Sample Input: "cbbd"
Sample Output: "bb"'''

def palindrome(str):
    if str==str[::-1]:
        return True

def main():
    inp=input('Enter a Text :')
    max_length=0
    ans=''
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            if palindrome(inp[i:j+1]):
                max_length=max(max_length,len(inp[i:j+1]))
                ans=inp[i:j+1]
    print(ans)
main()