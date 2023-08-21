'''
Adam Roy
Lab 12
Part 2
CSCI 160
'''

import os

def open_file(f):
    d = {}
    f = open(f, 'r')
    for line in f:
        x = line.strip('\n')
        (key, val) = x.split(':')
        d[(key)] = float(val)
    f.close()
    return d
    
def total_parts(f):
    i = 0
    for line in f:
        i += 1
    i -= 1
    i /= 2
    return int(i)
    
def parts_less_than(d):
    i = 0
    pLT = {}
    for (key, value) in d.items():
        if value <= 10:
            print(key, value)
              
def least_expensive_part(d):
    i = 10000000
    lEP = []
    for (key, value) in d.items():
        if value == i:
            lEP.append(key)
        elif value < i:
            lEP = []
            i = value
            lEP.append(key)
    return lEP
    
def most_expensive_part(d):
    i = 0
    mEP = []
    for (key, value) in d.items():
        if value == i:
            mEP.append(key)
        elif value > i:
            mEP = []
            i = value
            mEP.append(key)
    return mEP

def average_price(d):
    aP = 0
    i = 0
    for (key, value) in d.items():
        aP += value
        i += 1
    aP /= i
    return aP
    
def print_parts(d):
    for (key, value) in d.items():
        print(key)

def main():
    f = input('Enter a file name: ')
    if not os.path.isfile(f):
        print('The input file does not exist or is not vaild')
        os._exit(0)

    oF = open_file(f)
    tP = total_parts(f)
    print('\nTotal number of parts', tP)
    print('\nParts less than $10')
    pLT = parts_less_than(oF)
    lEP = least_expensive_part(oF)
    print('\nLeast expensive part\n', lEP)
    mEP = most_expensive_part(oF)
    print('\nMost expensive part\n', mEP)
    aP = average_price(oF)
    print('\nAverage Price', aP)
    print()
    print('Parts List:')
    pP = print_parts(oF)
    
    
main()
