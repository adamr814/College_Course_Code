'''
Adam Roy
Assignment 11
CSCI 160
'''

import os

def fill_dict(f):
    d = {}
    f = open(f, 'r')
    for line in f:
        x = line.strip('\n')
        (key, val) = x.split(':')
        d[(key)] = val
    return d

def find_word(d):
    inp = input('Enter an English word: ')
    w = 0
    while inp != '':
        w = d.get(inp)
        print('\nThe French translation is: ', w)
        inp = input('\nEnter an English word: ')
        
            

def main():
    f = str(input('Enter a file name: \n'))
    if not os.path.isfile (f):
        print('Input file is invalid or does not exist')
        os._exit(0)    
    
    fD = fill_dict(f)
    print('\nEnter an English word to receive the French translation: \nPress ENTER to quit.\n')
    fW = find_word(fD)
main()
    
