# Hangman Game
[View the live site here]( https://hangman-game-pp3-deb9aac8daff.herokuapp.com/)

## Mockups
![desktop-mockup](assets/images/mockup.png)
## Introduction
For my PP3, I have made a basic hangman game. The aim of the game is to guess the word within 10 guesses. 
# Game Features
## Username Feature
Upon visiting the site, the user is met with a welcome message and username prompt. This username must meet the specific criteria or else the user will receive an error message and the game will not begin. Once the username meets the stated criteria, the game options are presented. 
![intro](assets/images/username.png)

## Game Options
There are two options to choose from before the game begins, start and exit. 
### Exit 
If the user chooses to exit the game, a goodbye message is displayed and no further options are presented. 
![end-game](assets/images/end-game.png)
### Start 
If the user chooses to start the game, the below features are implemented; 
-	Game Hint 
The game tells the user that the words are based on musicial instruments. This is the only hint that the user is given throughout the game. 
-	Lives 
The user is told they have 10 lives before the game begins. 
The game is now ready to begin. 
## Game Play 
The user is presented with the letter count of the word they must guess and the amount of lives they have remaining. Once the user selects their first letter, the following features are implemented: 
-	Correct Guess 
If the user guesses a letter correctly, that letter replaces the corresponding blank space in the word, no lives lost. It then allows the user to guess again. 
![correct](assets/images/correct.png)

-	Incorrect Guess 

If the user guesses incorrectly, they are presented with an error message and their remaining life count. 
![incorrect](assets/images/incorrect.png)


-	Letter Previously Guessed 
If the user guesses a letter they have previously chosen, they are presented with an error message and asked to try again. The life count remains the same. 
![guessed](assets/images/guessed.png)


-	Lives Lost 
If the user loses their lives before the word is guessed, they are met with a condolence message and the option to restart or exit the game.
![lost-lives](assets/images/lost-lives.png)


### Game Won 
If the user guesses the word without losing all of their lives, they have won the game. 
Once the word is guessed – the user is presented with a congratulations message and confirmation of the guessed word. 
![won](assets/images/won.png)

They are then given two options, restart or return home. Restart will restart the whole game and return to home will prompt the user to exit which will give a goodbye message to the user. 
![end-options](assets/images/end-options.png)

## Features left to implement 
In the future, I would like to add the option of a hint for the user and also different levels of difficulty. 

