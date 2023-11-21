import random

# words to be used in the game
def choose_word():
    words = ["guitar", "piano", "flute", "violin", "drums", "bass", "triangle","clarinet","cello"]
    return random.choice(words)

# iterate through each letter in the word
# if guessed correctly - add letter to display string
# if guessed incorrectly, add an underscore to the display string
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
            print("Correct, well done!\n")
            continue
        else:
            display += " _ "
    return display

# select word at random - convert to lowercase
# keeps track of letters guessed 
# amount of guesses user has
def hangman():
    word_to_guess = choose_word().lower() 
    guessed_letters = []  
    attempts = 10 

# username function - error if requirements not met. Print to console when met
def welcome():
    print("Welcome to Hangman! This is a gussing game where you have a limited number of\n lives. Do you think you have what it takes?\n")
    while True:
        username = input("Enter your username below to get started! (1-8 characters, no numbers or special characters):\n")

        if 1 <= len(username) <= 8 and username.isalpha():
            break
        else:
            print("Username error, please try again.\n")

    print(f"Hello, {username}! Welcome to Hangman.\n")
    return username

# game options
def display_menu():
    print("Please select an option below:\n")
    print("1. Start Game")
    print("2. Exit Game/n")

# gets user choice of 1 or 2
def get_user_choice():
    choice = input("Enter your choice (1 or 2):\n")
    return choice

def start_game(username):
    objective = "The words used in this game are popular musical instruments. You have 10 lives. Good luck!\n"
    print(objective)
    
    # choose random word and set guessed letters to an empty set
    word_to_guess = choose_word().lower()
    guessed_letters = set()
    lives = 10
    # loop runs if word is not guessed - breaks if lives gone or word guessed
    while lives > 0:
        display_word_with_lives(word_to_guess, guessed_letters, lives)
        guess = get_user_guess()

        if guess in guessed_letters:
            print("Oops! You've already guessed that letter. Please try again.\n")
            continue  # Skip the rest of the loop and get a new guess

        guessed_letters.add(guess)

        if guess in word_to_guess:
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations, {username}! You guessed the word: {word_to_guess}\n")
                break
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}\n")

            if lives == 0:
                print(f"Oops! You ran out of lives./n The correct word was: {word_to_guess}.\nBetter luck next time!")

    end_game(username)

# get single letter input before game begins, error if requirements not met
def get_user_guess():
    while True:
        guess = input("Guess a letter: \n").lower()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Invalid input. Please enter a single letter.\n")

# users progress of lives and guesses 
def display_word_with_lives(word, guessed_letters, lives):
    print(f"Word: {display_word(word, guessed_letters)} | Lives: {lives}")

# end of game options
def end_game(username):
    print("Game Over! Want to try again?\n")
    print("Select an option:\n")
    print("1. Restart")
    print("2. Quit To Home\n")
    choice = get_user_choice()

    # action to be taken after user choice
    if choice == '1':
        start_game(username)
    elif choice == '2':
        print(f"Sure thing, {username}! Returning home..\n")
        return
    else:
        print("Invalid choice. Returning Home...\n")
        return   

# checks if script is being run as main program and not imported 
if __name__ == "__main__":
    # ensures that program keeps running and responding user's choices until they decide to quit the game
    username = welcome()

    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == '1':
            start_game(username)
        elif user_choice == '2':
            print(f"Goodbye, {username}! Hope to see you again soon!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")