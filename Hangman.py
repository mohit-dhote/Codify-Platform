# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.\n\n")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


#The functions input
#secret_word: string, the word the user is guessing
#letters_guessed: list, what letters have been guessed so far

def isWordGuessed(secret_word, letters_guessed):
    '''
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secret_word:
        if not (char in letters_guessed):
           return False
    return True


def getGuessedWord(secret_word, letters_guessed):
    '''
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    remin =''
    for char in secret_word:
        remin += (char if char in letters_guessed else '_ ')
    return remin    


def getAvailableLetters(letters_guessed):
    '''
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ''
    for char in all_letters:
        if not (char in letters_guessed):
            available_letters += char
    return available_letters        
    

#Start new guess round if could
def newGuess(letters_guessed,mistake_points):
    print('-------------')
    print('You have {} guesses left.'.format(mistake_points))
    print ('Available letters: {}'.format(getAvailableLetters(letters_guessed)))
    return input('Please guess a letter: ').lower()
    
def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    #Print welcome message
    #Print the secret word length
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secret_word)))

    #init guessed letters
    letters_guessed =[]

    #init mistake numbers
    mistake_points = 8

    while(mistake_points > 0 and not isWordGuessed(secret_word,letters_guessed)):
        new_letter = newGuess(letters_guessed,mistake_points)
        if new_letter in secret_word:
            if new_letter in letters_guessed:
                print('Oops! You\'ve already guessed that letter: {}'.format(getGuessedWord(secret_word,letters_guessed)))
            else:
                letters_guessed.append(new_letter)
                print('Good guess: {}'.format(getGuessedWord(secret_word,letters_guessed)))    
        else:
            mistake_points -= 1
            print('Oops! That letter is not in my word: '.format(getGuessedWord(secret_word,letters_guessed)))

    
    print('--------------')
    if(isWordGuessed(secret_word,letters_guessed)):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses.  The word was {}'.format(secret_word))                

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secret_word = chooseWord(wordlist).lower()
hangman(secret_word)
