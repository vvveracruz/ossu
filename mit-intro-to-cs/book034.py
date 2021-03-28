###############################################################################
#
#   27 March 2020
#   Chapter 3.3
#
#   Newton-Rhapson method for finding roots
#
###############################################################################

def nr_square_root( c, epsilon = 0.01, r = 100 ):
    '''
    Finding the square root of a number using the newton rhapson method
    '''
    print('\n\n       Newton-Rhapson Method\n')
    guess = c / 2
    counter = 0

    while abs( guess*guess - c ) >= epsilon:
        print('Round: ', counter, '    Guess: ', guess)
        # guess = round( guess - (( guess*guess - c  ) / ( 2 * guess )), r )
        guess = guess - (( guess*guess - c  ) / ( 2 * guess ))
        counter +=1 
    
    print('The square root of', c, 'is close to', guess)
    return guess

def bs_square_root(x, epsilon = 0.01):
    '''
    Finds the square root of a number x using bisection search
    '''
    print('\n\n       Bisection Search Method\n')
    num_guesses = 0
    low = 0.0
    high = max(1.0, x)
    guess = (high + low)/2

    while abs( guess**2-x ) >= epsilon:
        # print('low =', low, ', high =', high, ', guess =', guess)
        print('Round: ', num_guesses, '    Guess: ', guess)
        num_guesses += 1
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2

    print('The square root of', x, 'is close to', guess)
    return guess
    
nr_square_root(3242131.0)
bs_square_root(3242131.0)