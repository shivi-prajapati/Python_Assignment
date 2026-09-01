'''Assignment 3: Course Feedback Compiler & Sanitizer
Scenario
Student feedback records contain ratings from 1 to 5 stars. Due to raw data entry issues, the feedback database has 
some course entries with list values that are empty, or lists containing invalid elements (such as string annotations 
like "Excellent" or None values).

Problem Description
Write a function compile_feedback(ratings_dict) that processes course feedback:

The parameter ratings_dict is a dictionary where keys are course names (strings) and values are lists of ratings 
(which should be numeric but may contain invalid types).
The function must return a dictionary mapping each course name to its average rating, rounded to 2 decimal places.
Implement the following error handling criteria:
For each rating inside a course's list, attempt to convert it to a float. If a rating cannot be converted (throws a 
ValueError or TypeError), catch the exception, print a warning: "Warning: Invalid rating value '<val>' in course 
'<course>' skipped.", and continue processing the rest of the list.
If a course has no valid ratings (the list is empty or contains no convertible numbers), computing the average will 
rigger a division-by-zero error. Catch ZeroDivisionError, print a warning: "Warning: No valid ratings found for course 
'<course>'. Rating set to 0.0.", and assign the course an average rating of 0.0.'''

def compile_feedback(ratings_dict,key):
    print(ratings_dict)
    sum=0
    count=0
    for fetch_value in ratings_dict.get(key):
        try:
            if not int(fetch_value): 
                ...          
        except ValueError:
            print(f'Warning: Invalid rating value {fetch_value} in course {key} skipped.')
        else:
            count+=1
            sum+=int(fetch_value)
    try:
        avg=sum/count
    except ZeroDivisionError:
        print(f"No valid  rating found for {key} rating set to 0.0")
    else :print(avg)
    
def main():
    feedback={}
    key=input('Enter a Course name :')
    value=[]
    while True:
        value1=input('Enter rating :')
        value.append(value1)
        confirm=input('You Want to add more ratings (y/n) :')
        if confirm=='n':
            break
    feedback[key]=value
    compile_feedback(feedback,key)
main()