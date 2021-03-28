###############################################################################
#
#   24 March 2020
#   Chapter 3.3
#
#   Search algorithms for roots
#
###############################################################################

import time

def is_int( s ):
    try:
        int(s)
        return True
    except ValueError:
        return False

# x = input('Enter an integer: ')
# while not is_int(x):
#     x = input('Enter an integer: ')

def exhaustive_enum( x, epsilon = 0.01, step = 0.01**2):
    '''
    Finds the square root of a number x using exhaustive ennumeration
    '''
    num_guesses = 0
    guess = 0.0

    while abs( guess**2 - x ) >= epsilon  and guess <= x :
        guess += step
        num_guesses +=1
    print('Number of guesses', num_guesses)
    # loop exited when the guess is close enough to the actual root
    #       or the guess for the root has become bigger than the square itself

    if guess**2 - x >= epsilon:
        print('No approximation found for the square root of', x)
        return None
    else:
        print(guess, 'is close to the square root of', x)
        return guess

def bisection_search(x, epsilon = 0.01):
    '''
    Finds the square root of a number x using bisection search
    '''
    num_guesses = 0
    low = 0.0
    high = max(1.0, x)
    guess = (high + low)/2

    while abs( guess**2-x ) >= epsilon:
        print('low =', low, ', high =', high, ', guess =', guess)
        num_guesses += 1
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2

    print('Number of guesses', num_guesses)
    print(guess, 'is close to the square root of', x)
    return guess

def get_ordinal(n):
    '''
    Returns the appropriate ordinal string for a number n. 
    '''
    n = str(n)

    if n[-1]+n[-2] == '11' or n[-1]+n[-2] == '12' or n[-1]+n[-2] == '13':
        ordinal = n + 'th'
    elif n[-1] == '1':
        ordinal = n + 'st'
    elif n[-1] == '2':
        ordinal = n + 'nd'
    elif n[-1] == '3':
        ordinal = n + 'rd'
    else:
        n + 'th'
    
    return ordinal
    
def n_bisection_search(x, epsilon = 0.01, n = 3):
    '''
    Finds the nth root of a number x using bisection search.

    I think this should work but I haven't really tested it beyond n = 3.
    '''
    num_guesses = 0
    low = min(-1, x)
    high = max(1.0, x)
    guess = (high + low)/2

    while abs( x-guess**n ) >= epsilon:
        print('low =', low, ', high =', high, ', guess =', guess)
        num_guesses += 1
        if guess**n < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2
        # time.sleep(1)

    print('Number of guesses', num_guesses)
    print(guess, 'is close to the,', get_ordinal(n) ,'root of', x)
    return guess

n_bisection_search(27, 0.01, 23)