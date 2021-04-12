###############################################################################
#
#   12 April 2021
#   Chapter 4.1.1
#
#   A function that accepts two strings as arguments and returns True if
#   either string occurs anywhere in the other, and False otherwise
#
###############################################################################

def isIn( str1, str2 ):
    if str1 in str2:
        return True
    else:
        return False

print(isIn('hello', ' hello '))