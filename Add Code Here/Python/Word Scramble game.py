import random

def word_scramble():
    words = ["python", "programming", "hangman", "computer", "keyboard"]
    word_to_guess = random.choice(words)
    scrambled_word = list(word_to_guess)
    random.shuffle(scrambled_word)
    scrambled_word = "".join(scrambled_word)

    print(f"Unscramble this word: {scrambled_word}")
    guess = input("Your guess: ")

    if guess == word_to_guess:
        print("Congratulations! You unscrambled the word.")
    else:
        print(f"Sorry, the word was: {word_to_guess}")

word_scramble()
