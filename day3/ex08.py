'''Exercise 8: De-duplicating Shopping Cart
Scenario: An online shopping cart has duplicate items due to double-clicks: ["apple", "banana", "apple", 
"orange", "banana", "banana"]. Write a program that processes the list and removes all duplicate items, 
but keeps the first occurrence of each item in its original order. Print the cleaned cart.

Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange']'''

def de_duplicating():
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    frq={}
    cart_new=[]
    for i in cart:
        frq[i]=frq.get(i,0)+1
    for i in frq:
        if frq[i]>=1:
            cart.pop(cart.index(i))
            cart_new.append(i)
    print(cart_new)   
de_duplicating()

    


