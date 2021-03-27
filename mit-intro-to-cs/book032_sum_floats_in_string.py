###############################################################################
#
#       23 March 2021
#       Finger exercises, chpt 3.2
#
#       Let s be a string that containes a sequence of decimal numbers
#       separated by commas, e.g., s = '1.23, 2.4, 3.123'. Write a program that
#       prints the sum of the numbers in s.
#
###############################################################################

s = '1.23,2.4,3.123'

floats_list = []
f = ''
for c in s:
    if c == ',':
        floats_list.append( float(f) )
        #print( 'floats_list', floats_list )
        f = ''
    else:
        f += c
        #print('f', f)
        
# catching the last float since there is no comma after it
floats_list.append( float(f) )

n = 0
for f in floats_list:
    n += f

print( 'The sum of the numbers in', s, 'is', n )
