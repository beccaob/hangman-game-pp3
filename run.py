import random

# words to be used in the game
def choose_word():
    words = ["guitar", "piano", "flute", "violin", "drums", "bass", "triangle"]
    return random.choice(words)

# iterate through each letter in the word
# if guessed correctly - add letter to display string
# if guessed incorrectly, add an underscore to the display string
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
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
    print("Welcome to Hangman!")
    while True:
        username = input("Enter your username (1-8 characters, no numbers or special characters):\n")

        if 1 <= len(username) <= 8 and username.isalpha():
            break
        else:
            print("Username error, please try again.")

    print(f"Hello, {username}! Welcome to Hangman.")
    return username


        