# Snake_Game
A simple python snake game using turtle library

This is a Python code that creates a simple game of Snake using the turtle module. The game consists of a snake that moves around the screen eating food and growing longer. The game ends if the snake hits the wall or its own body.

The code starts by importing the turtle and random modules. The variables h, a, b, fcoord, and pos are all initialized to their default values. Function "home" starts the game by setting some of the variables to their initial values, clearing the turtle screen, and drawing the "Play" text. Function "level_1" is used to draw the game board on the screen.

Function "start" is the core of the game, it listens to keyboard events to move the snake around the game board. It also updates the score when the snake eats the food and ends the game when the snake hits the wall or its own body.

Function "food" randomly selects a location on the game board to place the food that the snake eats. Functions "u", "d", "l", and "r" are used to move the snake in the desired direction. Finally, "move" function moves the snake in the direction specified by the keyboard events.

Function "gameover" is called when the game ends, it displays the "Game Over" text and the final score. Then it waits for a click event to return to the main menu.

The last part of the code checks if the current file is the main module, and if so, it starts the game by calling function "home".

I created the functions as the following:
home(x,y): This function resets all the variables and clears the turtle screen to display the start message "Play". It sets the on-screen click event to the start() function.

game(): This function draws the borders of the game using the turtle module.

start(x,y): This function is called when the player clicks on the screen to start the game. It calls the level_1() function to draw the borders and initializes the food and score turtles. It then enters a loop that listens to the player movement keys (Up, Down, Left, Right) and calls the move() function to update the position of the snake. If the snake intersects with the food, the score is incremented, and a new food is generated. If the snake intersects with its own body, the game ends.

food(tfood): This function generates random coordinates for food on the screen and moves the turtle object to that position.

u(): This function changes the orientation of the snake to move up.

d(): This function changes the orientation of the snake to move down.

l(): This function changes the orientation of the snake to move left.

r(): This function changes the orientation of the snake to move right.

move(): This function updates the position of the snake by moving it one step forward and storing its current position. If the snake has grown, it removes the last stored position. If the snake has intersected with its own body, the game ends.

gameover(): This function is called when the game ends. It displays the "Game Over" message and the final score and sets the on-screen click event to the home() function.





