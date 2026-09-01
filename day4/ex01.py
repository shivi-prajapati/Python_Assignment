'''Assignment 1: Inventory Tracker for CDAC Bookstore
Scenario
The CDAC Bookstore needs a backend helper module to manage books and their quantities. 
The inventory is stored in a Python dictionary where keys are book titles (strings) and 
values are quantities in stock (non-negative integers).'''

def manage_bookstore_inventory(inventory,action,title,quantity=0):
    inventory={"Python":10,"Ai":5,"Java":0}
    if action=="add":
        add(inventory,action,title)
    if action=="lookup":
        lookup(inventory,action,title)
    if action=="sell":
        sell(inventory,action,title)
        
            
def add(inventory,action,title):
    quantity_book=int(input('Enter a Quantity :'))
    if title in inventory:
        new_quantity=inventory.get(title)+quantity_book
        inventory[title]=new_quantity
    else:
        inventory[title]=quantity_book
    print(inventory)

def lookup(inventory,action,title):
    try:
        if title in inventory:
            print(inventory.get(title))
    except:
        print(f"{title}=0")

def sell(inventory,action,title):
    quantity_book=int(input('Enter a Quantity :'))
    
    if title in inventory:
            if quantity_book<=inventory.get(title):
                total=inventory.get(title)-quantity_book
                print(total)
            elif inventory.get(title)==0:
                inventory.pop(title)
                print(inventory)
            else:
                print(f"Error: Insufficient stock for{title}'. Available: {inventory.get(title)}")
    else:
            print(f"Error: Book '{title}' not found in inventory.")

       
def main():
    user='yes'
    while user=='yes':

       inventory={"Python":10,"Ai":5,"Java":0}
       action_book=input('Enter a  Action :').lower()
       title_book=input('Enter a Title of Book :').title()
       manage_bookstore_inventory(inventory,action_book,title_book)
       user=input("You want to coninue: yes/no")
main()
