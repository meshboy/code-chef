__author__ = 'meshboy'

# this program accepts numbers and reverse them

def reverse_number(number):
    return int(number[::-1])

myList = []

t = raw_input()

for count in range(int(t)):
    myList += [reverse_number(raw_input()), ]

for a in myList:
    print a