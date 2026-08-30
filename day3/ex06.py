'''Exercise 6: Grading on a Curve
Scenario: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated 
test scores. Convert them to a list of integers. Using a single list comprehension with conditionals, 
apply the following curve rules:

If a score is below 50, add 10 points.
If a score is 50 or higher, add 5 points.
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103). Print the original and the curved grades.
Sample Input: "45 88 30 98 50"
Sample Output:
Original: [45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]'''


def grading():
    score = list(map(int, input('Enter space separated test scores :').split()))
    list1=[]
    list1=score
    list1=[i+10 if i<50 
          else i+5 if i+5<=100 
          else 100
          for i in score
          ]
    print(list1)
grading()
           
            
    
    


