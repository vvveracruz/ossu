###############################################################################
#
#       22 March 2021
#
#       Finger exercises, chpt 3.1
#
###############################################################################

import itertools

def is_int( s ):
    try:
        int(s)
        return True
    except ValueError:
        return False

x = input('Enter an integer: ')
while not is_int(x):
    x = input('Enter an integer: ')

x = int(x)

for pwr, root in itertools.product(range(2, 6), range(1, x)):
    if root**pwr == x:
        break

if root**pwr == x:
    print('I found root =', root, 'and pwr =', pwr, 'for x =', x, '\n')
else:
    print('No root and pwr could be found for x =', x, '\n')
