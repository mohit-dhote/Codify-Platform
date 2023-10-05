import random

# List of words to be scrambled
word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "blueberry"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to scramble a word
def scramble_word(word):
    word_chars = list(word)
    random.shuffle(word_chars)
    return ''.join(word_chars)

# Main game loop
while True:
    # Choose a random word and scramble it
    target_word = choose_word()
    scrambled_word = scramble_word(target_word)

    print("Unscramble the word:", scrambled_word)

    # Ask the player to guess the unscrambled word
    guess = input("Your guess: ")

    if guess.lower() == target_word:
        print("Correct! The word is:", target_word)
    else:
        print("Incorrect. The word is:", target_word)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
