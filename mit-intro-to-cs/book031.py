###############################################################################
#
#       22 March 2021
#
#       Finger exercises, chpt 3.1
#
###############################################################################

import itertools

while True:
    try:
        x = int(input('Enter an integer: '))
        break
    except ValueError:
        print('Ding dong you\'re wrong. You can only enter integers. Try again.')
        continue

for pwr, root in itertools.product(range(2, 6), range(1, x)):
    if root**pwr == x:
        break

if root**pwr == x:
    print('I found root =', root, 'and pwr =', pwr, 'for x =', x)
else:
    print('No root and pwr could be found for x =', x)
