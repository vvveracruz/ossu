###############################################################################
#
#   24 March 2020
#   Chapter 3.3
#
#   Search algorithms for cube roots
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

def bisection_search(x, epsilon = 0.01):
    num_guesses = 0
    low = min(-1, x)
    high = max(1.0, x)
    guess = (high + low)/2

    while abs( x-guess**3 ) >= epsilon:
        print('low =', low, ', high =', high, ', guess =', guess)
        num_guesses += 1
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2
        time.sleep(1)


    print('Number of guesses', num_guesses)
    print(guess, 'is close to the cube root of', x)
    return guess

bisection_search(27)
bisection_search(-27)
