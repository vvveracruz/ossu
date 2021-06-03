###############################################################################
#
#   May 2021
#   Problem Set 2
#
#   Implementing a game of hangman as described here:
#   https://en.wikipedia.org/wiki/Hangman_(game)
#
#   > TESTING
#   The testing module is called tests, and the testing functions have the same
#   name as the corresponding game functions.
#
###############################################################################
import random
import string
import tests

#   global variables
WORDLIST_FILENAME = "words.txt"
GUESS_TO_LEN_RATIO = 1.5

#   helper functions
def load_words():
    '''
    Returns a list of valid words. Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(">", len(wordlist), 'words loaded.')
    return wordlist

def choose_word(wordlist):
    '''
    Returns a word from a wordlist at random.
    '''
    return random.choice(wordlist)

# game functions
def is_word_guessed(secret_word, letters_guessed):
    '''
    Input:  secret_word (str):      the word to be guessed 
            letters_guessed (str):  the characters that have 
                                    been guessed by the player
    Returns a True if all letters of secret_word are in letters_guessed.
    '''
    

def play():
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    # user is given a certain number of guesses at the beginning (prop to the length of the word?)
    # info printed about the game, number of guesses left etc
    # user inputs guess then 
    # loop  a) reveals the letter if it is in the word
    #       b) penalises the user if it isnt and displays the number of guesses remaining
    # game ends when guesses is 0 or word is guessed


if __name__ == "__main__":
    #play()