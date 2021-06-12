# June 2021

import random
import string

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

if __name__=="__main__":
    # secret_word = choose_word()
    secret_word = 'apple'
    letters_guessed = 'ale'

    print(get_available_letters(letters_guessed))
