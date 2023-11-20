# randomly chose a word from list 
import random

# words to be used in game
def choose_word():
    words = {"guitar","piano","flute","violin","drums","bass","triangle"}
    return random.choice(words)

# iterate through each letter in the word
# if guessed correctly - add letter to display string
# if guessed incorrectly, add an underscore to display string

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

#select word at random - convert to lowercase
#keeps track of letters guessed 
#amount of guesses user has

def hangman():
    word_to_guess = choose_word().lower() 
    guessed_letters = []  
    attempts = 10 

# username function - error if requirements not met. Print to console when met

def welcome():
    print("Welcome to Hangman!")
    while True:
        username = input("Enter your username (1-8 characters, no numbers or special characters):\n")

        if 1 <= len(username) <= 8 and username.isalpha():
            break
        else:
            print("Username error, please try again.")

    print(f"Hello, {username}! Welcome to Hangman.")

#game options
def display_menu():
    print("Please select an option below:")
    print("1. Start Game")
    print("2. Exit Game")

#gets user choise of 1 or 2
def get_user_choice():
    choice = input("Enter your choice (1 or 2):\n")
    return choice

def start_game():
    objective = "The words used in this game are popular musical instruments. You have 10 lives. Good luck!"
    print(objective)

    word_to_guess = choose_word().lower()
    guessed_letters = []
    lives = 10

    while lives > 0:
        display_word_with_lives(word_to_guess, guessed_letters, lives)
        guess = get_user_guess()

        if guess in guessed_letters:
            print("Oops! You've already guessed that letter. Please try again.")

        elif guess in word_to_guess:
            guessed_letters.append(guess)
            if "_" not in display_word(word_to_guess, guessed_letters):
                print(f"Congratulations, {username}! You guessed the word: {word_to_guess}")
                break
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

        