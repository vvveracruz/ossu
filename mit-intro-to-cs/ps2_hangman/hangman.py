###############################################################################
#
#   18 April 2021
#   Problem Set 2
#
#   Implementing a game of hangman as described here:
#   https://en.wikipedia.org/wiki/Hangman_(game)
#
#   the computer selects a word t random from the list of available words 
#   in words.txt
#   user is given a certain number of guesses
#   the user inputs guesses and the computer either
#       a) reveals the letter if it exists
#       b) penalises the user and updates the number of guesses remaining
#   the game ends when the user guesses the word or they run out of guesses
#
###############################################################################
import random
import string
import tests

#   ---------------------------------------------------------------------------
#   global variables
WORDLIST_FILENAME = "words.txt"

#   ---------------------------------------------------------------------------
#   helper functions
def load_words():
    '''
    Returns a list of valid words. Depending on the size of the word list, this function may
    take a while to finish.

                  Name            Type            Comment
                  ----            ----            -------
    Input     |   None        |               |
    Output    |   wordlist    |   lst[str]    |   words are strings of lowercase letters
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

                  Name            Type            Comment
                  ----            ----            -------
    Input     |   wordlist    |   lst[str]    |   
    Output                    |   str         |   string of lowercase letters
    '''
    return random.choice(wordlist)

#   ---------------------------------------------------------------------------
#   gameplay functions
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    Checks whether all the letters in secret_word are in letters_guessed.

    Input     |   secret_word     |   str         |   all chars are lowercase
    Input     |   letters_guessed |   lst[chars]  |   all chars are lowercase
              -                   -               -
    Output                        |   boolean     |   
    '''
    for i in range(len(secret_word)):
        if secret_word[i] != letters_guessed[i]:
          return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
