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

#gets user choice of 1 or 2
def get_user_choice():
    choice = input("Enter your choice (1 or 2):\n")
    return choice

if __name__ == "__main__": #checks if being run directly or imported as a module
    welcome()

    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == '1':
            start_game()
        elif user_choice == '2':
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def start_game():
    objective = "The words used in this game are popular musical instruments. You have 10 lives. Good luck!"
    print(objective)
#choose random word and sets guessed letters to 0 
    word_to_guess = choose_word().lower()
    guessed_letters = []
    lives = 10
# loop runs if word is not guessed - breaks if lives gone or word guessed
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

        if lives == 0:
            print(f"Oops! You ran out of lives. The correct word was: {word_to_guess}. Better luck next time!")

        end_game()
    
def display_word_with_lives(word,guessed_letters,lives):
    print(f"Word: {display_word(word, guessed_letters)} | Lives: {lives}")

def get_user_guess():
    return input("Guess a letter: ").lower()

def end_game():
    print("Game Over")
    print("Select an option:")
    print("1. Restart")
    print("2. Quit")
    choice = get_user_choice()

    if choice == '1':
        start_game()
    elif choice == '2':
        print(f"Goodbye, {username}!")
        exit()
    else:
        print("Invalid choice. Exiting...")
        exit()

        