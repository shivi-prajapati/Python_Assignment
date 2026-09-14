'''Exercise 10: Snake Game Board Renderer
Scenario: Render a simple 2D text game board. Write a program that performs the following steps in sequence:

Creates a 
5
×
5
 grid filled with dots "." represented as a nested list.
Places a food item "F" at grid position [2, 3].
Prompts the user to enter coordinate inputs: a row and a col (integers between 0 and 4) for the snake's head.
Places the snake's head "S" at the user-supplied coordinate [row, col], overwriting the character at that position.
If the user-supplied coordinates are exactly [2, 3], print the message "Yum! The snake ate the food!" (the snake "S" will occupy index [2, 3] on the printed board, overwriting the "F").
Prints the grid neatly line-by-line (each row's elements separated by spaces).'''


def main():
    snake_pos=input("Enter the position of snake in the (x,y) format: ")
    snake_pos=tuple([int(n) for n in snake_pos.split(",")])
    food=(2,3)
    ch="  .  "
    for i in range(5):
        for j in range(5):
            if(i,j)==snake_pos:
                ch="  S  "
            elif (i,j)==food:
                ch="  F  "
            else:
                ch="  .  "
            print(ch,end="")
        print()
    if(snake_pos==food):
        print("Yum! The snake ate the food")
main()