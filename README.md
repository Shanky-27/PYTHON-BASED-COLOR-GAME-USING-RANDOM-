Color Game - Tkinter Application
Overview
The Color Game is a simple yet engaging application built using Python's Tkinter library. The game challenges the player to correctly identify the color name displayed on the screen. However, the text color of the name might not match the color it names, which adds a layer of difficulty. The game keeps track of the player's score, rewarding correct answers.

Features
Color Matching: The game displays a color name in a random color, and the player must choose the correct color name from a set of buttons.
Score Tracking: The game keeps track of the player's correct answers.
Dynamic Color Updates: After each guess, the game updates the color and text for the next round.
Instant Feedback: The game provides immediate feedback on whether the player's choice was correct or incorrect.
Prerequisites
Python 3.x installed on your system.
Tkinter library (included with standard Python installations).
How to Run
Execute the Python script to start the Color Game:

python color_game.py
The game window will open, and you can start playing immediately.

Game Instructions
Start the Game: Once the game window opens, a color name will be displayed in a randomly chosen color.
Make a Guess: Click on the button that corresponds to the color name displayed. For example, if the text says "red" but is colored blue, you should click the "red" button.
Feedback: After each selection, the game will indicate whether your choice was correct or incorrect, and then display a new color name for the next round.
Scoring: Your score increases by 1 for each correct answer. The game continues indefinitely, allowing you to improve your score.
File Structure
color_game.py: The main Python file containing the code for the Color Game.
README.md: This file provides an overview of the application and instructions on how to run it.
Code Explanation
Main Components:

ColorGame: The main class that initializes the game, handles user interactions, and updates the game state.
update_color(): Updates the color name and its display color randomly for the next round.
check_answer(selected_color): Checks if the player's selected color matches the displayed color name and updates the score accordingly.
clear_status(): Clears the status label after a short delay to prepare for the next round.
UI Setup:

The game window consists of a label displaying the color name, a set of buttons for color choices, and a status label to show whether the previous answer was correct.
