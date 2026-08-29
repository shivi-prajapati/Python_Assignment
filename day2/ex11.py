'''Exercise 11: Group Anagrams
Write a program that starts with a list of strings defined at the top of your script (e.g., words = ["eat", "tea", "tan", "ate", "nat", "bat"]) and groups the anagrams (words formed by rearranging letters) together. Print the final grouped list of lists.

Hardcoded Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]'''

def string_comp():
    inp=input('Enter a Text:').split()
    list=[]
    for i in inp:
        found=False
        for grp in list:
            if sorted(i)==sorted(grp[0]):
                grp.append(i)
                found=True
                break
        if found==False:
            list.append([i])
    print(list)
string_comp()

