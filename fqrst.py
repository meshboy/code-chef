__author__ = 'meshboy'

import math

# this program outputs the square root of numbers

t = raw_input()

result = ''

for count in range(int(t)):
    testCase = raw_input()

    result += str(int(math.sqrt(int(testCase)))) + "\n"

print result