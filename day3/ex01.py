'''Exercise 1: The Wizard's Magic Bag
Scenario: A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]. When the wizard steps through a magic portal, two things happen:

A new item enters the bag (prompts the user to input the item name to append to the end).
The oldest item in the bag (at index 0) is dissolved and ejected. Write a program to simulate this portal transition and print the final bag contents.
Sample Input: (User inputs "amulet")
Sample Output:
Portal transition activated!
Ejected oldest item: staff
Current items in the magic bag: ['potion', 'spellbook', 'amulet']'''

def magic_bag():
    inp=(input('Enter Item Name :')).split()
    list=[]
    list=inp
    
    str=input('Enter a Word You want to append :')
    print('Portal transition activated!')
    if str!='':
        list.append(str)
        str_remove=list.pop(0)
        print(f'Ejected oldest item :{str_remove}')
    print(f'Current items in the bag :{list}')
magic_bag()



