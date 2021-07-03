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
    print('\n')
    if guesses == 1:
        print('Last chance: you have 1 guess left.')
    else:
        print('You have '+str(guesses)+' wrong guesses left.')
    print('Available letters: '+get_available_letters(letters_guessed)+'.')
    return None
    
def match_with_gaps(guessed_word, other_word):
    # checks whether guessed_word could be other_word
    guessed_word = guessed_word.replace(' ', '')
    if len(guessed_word) != len(other_word):
        return False

    letters_guessed = ''.join(set(guessed_word)) # unique letters in secret word

    for i in range(len(guessed_word)):
        if guessed_word[i]==other_word[i]:
            pass
        elif guessed_word[i]=='_' and other_word[i] not in letters_guessed:
            pass
        else:
            return False

    return True

def show_possible_matches(guessed_word):
    L = []
    for word in _WORDLIST:
        if match_with_gaps(guessed_word, word):
            L.append(word)
    if len(L)==0:
        return 'No matches found.'
    else:
        return L
        
def display_loss(secret_word):
    print('\nSorry, you lost. The secret word was', secret_word+'.\n\n')

def display_win(score):
    print(f'\nNice, you won. \nYou scored {score}\n')

def show_hint(guessed_word):
    print('Possible word matches are:\n', show_possible_matches(guessed_word))

def play(secret_word):
    guesses = math.ceil(len(secret_word))
    letters_guessed = ''
    print(
        '\n\n'
        '------------------------------------------------------------------\n'
        'Welcome to Ve\'s game of hangman\n'
        'I am thinking of a word that is '+str(len(secret_word))+' letters long.'
        )
    
    # main loop
    while guesses != 0:
        get_update_message(guesses, letters_guessed)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        letters_guessed += guess
        if guess == '*':
            show_hint(guessed_word)
        while len(guess) != 1 or guess not in string.ascii_lowercase:
            guess = input('Please guess a one single lowercase letter: ')
        if guess in secret_word:
            print('Good guess!')
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            guesses -= 1
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        score = guesses * len(''.join(set(secret_word))) # unique letters in secret word
        if secret_word == guessed_word.replace(' ', ''):
                display_win(score)
                break
        if guesses == 0:
            display_loss(secret_word)

if __name__=="__main__":
    secret_word = choose_word()
    #secret_word = 'apple'

    play(secret_word)
