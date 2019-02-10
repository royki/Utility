#!\C:\Python27

# Number to guess: How many iterations of an
# empty loop can we go through in a second?

def f(NUMBER):
    d = {}
    for i in xrange(NUMBER):
        d[i % 1000] = i

import sys
f(int(sys.argv[1]))