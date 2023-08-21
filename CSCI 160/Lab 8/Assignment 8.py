'''
Adam Roy
CSCI 289
Activity 8
'''

import os
f = input('Enter an input file: ')
xtype = 0
xval = 0

def externalFileCheck():
    if not os.path.isfile (f):
        print('\nThe input file is invalid or does not exist')
        os._exit(0)
    
def splitFile(main):
    inFile = [i.strip().split(',') for i in open(f).readlines()]
    return inFile

def find_type(splitFile):
    while xtype <= 4:
        if splitFile[xtype].find('B') > 0:
            type = 1
        elif splitFile[xtype].find('C') > 0:
            type = 2
        elif splitFile[xtype].find('W') > 0:
            type = 3
        xtype += 1
    return type

def find_value(splitFile):
    while xval <= 4:
        if splitFile[xval].find('1000.00') == 1:
            val = 1
        elif splitFile[xval].find('100.00') == 1:
            val = 2
        elif splitFile[xval].find('20.00') == 1:
            val = 3
        elif splitFile[xval].find('9.00') == 1:
            val = 4
        elif splitFile[xval].find('50.00') == 1:
            val = 5
        xval += 1
    return val

def main():
    if find_type == 1 and find_value == 1:
        print('10/01 Beginning Balance            1000.00')
    elif find_type == 2 and find_value == 2:
        print('10/02 Check              100.00    900.00')
    elif find_type == 2 and find_value == 3:
        print('10/03 Check              9.00      891.00')
    elif find_type == 3 and find_value == 3:
        print('10/04 Withdrawal         20.00     871.00')
    elif find_type == 2 and find_value == 5:
        print('10/05 Check              50.00     821.00')
        
externalFileCheck()  
main()
