__author__ = 'meshboy'

# this program adds the last number and first number

t = raw_input()

count = 0
result = ''

while count < int(t):

    count += 1

    testCase = raw_input()

    result += str(int(testCase[0]) + int(testCase[::-1][0])) + "\n"

print result
