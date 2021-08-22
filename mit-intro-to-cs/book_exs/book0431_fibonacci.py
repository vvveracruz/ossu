###############################################################################
#
#   16 April 2021
#   Chapter 4.3.1
#
#   Given the implementation of `fib` below, how many times does it compute the
#   the value of `fib(2)`` on the way to computing `fib(5)`?
#
###############################################################################

def fib(n):
    '''
    Assumes n                   int > 0 
    Returns Fibonacci of n      int > 0
    '''
    if n == 0 or n == 1:
        return 1
    else: 
        # if n-1 == 2 or n-2 == 2:
        #     print('fib(2) called')

        return fib(n-1) + fib(n-2)

def test_fib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))