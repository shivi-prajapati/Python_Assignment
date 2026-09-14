'''Exercise 9: The Josephus Elimination Game
Scenario: A group of 
N soldiers (numbered 1 to N) stand in a circle. Starting from the first soldier, every K-th soldier is 
eliminated from the circle. The count continues with the next remaining soldier, moving 
clockwise. This process repeats until only one soldier remains. Write a program that prompts the user 
to enter N(number of soldiers) and K(elimination interval). Simulate the game using a list and print 
the order of eliminations and the final survivor.

Sample Input: N = 5, K = 2
Sample Output:
Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
Eliminated soldier: 4 (Remaining: [1, 3, 5])
Eliminated soldier: 1 (Remaining: [3, 5])
Eliminated soldier: 5 (Remaining: [3])
The sole survivor is: 3'''

def main():
    n=int(input("Enter N value: "))
    k=int(input("Enter K value: "))

    l=[]
    for i in range(n):
        l.append(i+1)
    for j in range(1,k+1):
        for i in range(n):
            ind=i+k-j
            if ind<len(l):
                print(f"The value that will be deleted is: {l[ind]}    |   ",end=" ")
                del(l[ind])
                print(f"The remaining list is: {l}")


    print(f"The final remaining list: {l}")
main()



