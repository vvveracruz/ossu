# June 2021

import random
import string
import math

WORDLIST_FILENAME = 'words.txt'

def load_words():
    '''
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print('>', len(wordlist), 'words loaded.')
    return wordlist

_WORDLIST = load_words()

def choose_word():
    return random.choice(_WORDLIST)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, 
        the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), 
        which letters have been guessed so far; 
        assumes that all letters are lowercase
    returns: boolean, 
        True if all the letters of secret_word are in letters_guessed;
        False otherwise
    '''
    for char in secret_word:
        if char in letters_guessed:
            pass
        else:
            return False
    
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, 
        the word the user is guessing
    letters_guessed: list (of letters), 
        which letters have been guessed so far
    returns: string, 
        comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
    '''
    # return letters and underscores representing which letters have been guessed so far
    guessed_word = ''
    delimiter='_'

    for char in secret_word:
        if char in letters_guessed:
            guessed_word+=char
        else:
            guessed_word+=delimiter
        guessed_word+=' '
    
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), 
        which letters have been guessed so far
    returns: string (of letters), 
        comprised of letters that represents which letters have not
        yet been guessed.
    '''
    all_lowercase = string.ascii_lowercase
    available_letters = ''

    for char in all_lowercase:
        if char in letters_guessed:
            pass
        else:
            available_letters+=char
    
    return available_letters

def get_update_message(guesses, letters_guessed):
    print(
        'You have '+str(guesses)+' wrong guesses left.\n'
        'Available letters: '+get_available_letters(letters_guessed)+'.\n'
    )
    return None
    

def play(secret_word):
    guesses = math.ceil(len(secret_word)*0.4)
    letters_guessed = ''
    print(
        '\n\n'
        '------------------------------------------------------------------\n'
        'Welcome to Ve\'s game of hangman\n'
        'I am thinking of a word that is '+str(len(secret_word))+' letters long.\n'
        '\n'
        )
    
    # main loop
    while guesses != 0:
        get_update_message(guesses, letters_guessed)
        guess = input('Please guess a letter: ')
        while len(guess) != 1:
            guess = input('Input not valid.\nPlease guess a letter: ')
        if guess in secret_word:
            print('Good guess!')
            letters_guessed += guess
            print(get_guessed_word(secret_word, letters_guessed))
        guesses -= 1


if __name__=="__main__":
    secret_word = choose_word()
    # secret_word = 'apple'

    play(secret_word)
