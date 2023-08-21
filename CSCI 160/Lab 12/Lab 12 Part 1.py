'''
Adam Roy
Lab 12
Part 1
CSCI 160
'''

import os

def create_parts_list():
    key = 0
    value = 0
    d = {}
    while key != '' or value != '':
        key = input('Enter a part name: ')
        if key == '':
            return d
        value = input('\nEnter the price for the part: ')
        print()
        d[(key)] = value
    return d
        
def main():
    cL = create_parts_list()
    f = input('Enter a file name: ')
    if not os.path.isfile (f):
        print('The output file does not exist or is not valid')
        os._exit(0)
    f = open(f, 'w')
    for key, value in cL.items(): 
        f.write('%s:%s\n' % (key, value))
    f.close()
        
       
main()
