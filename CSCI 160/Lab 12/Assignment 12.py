'''
Adam Roy
Assignment 12
CSCI 160
'''

import os

def split_word(f):
    f = open(f, 'r')
    fL = []
    for line in f:
        x = line.strip('\n')
        x = x.replace(',', '').replace(' ', '').replace('.', '').lower()        
        temp = [char for char in x]
        fL.extend(temp)
        fL.sort()
    return fL

def create_dict(sW):
    d = {}
    i = 0
    val = 1
    for i in range(0, len(sW)):
        key = sW[i]
        d[(key)] = val
        i += 1
    return d

def adjust_dict(d, sW):
    i = 0
    for i in range(0, len(sW)):
        if sW[i] == sW[i-1]:
            x = d.get(sW[i])
            x += 1
            d[sW[i]] = x 
            i += 1

def highest_count(d):
    i = 0
    hCL = []
    for (key, value) in d.items():
        if value == i:
            hCL.append(key)
        elif value > i:
            hCL = []
            i = value
            hCL.append(key)
    return hCL
    
def lowest_count(d):
    i = 1000000
    lCL = []
    for (key, value) in d.items():
        if value == i:
            lCL.append(key)
        elif value < i:
            lCL = []
            i = value
            lCL.append(key)
    return lCL    




def main():
    f = str(input('\nEnter a file name: '))
    if not os.path.isfile (f):
        print('\nInput file is invalid or does not exist')
        os._exit(0)
        
    sW = split_word(f)
    cD = create_dict(sW)
    aD = adjust_dict(cD, sW)
    hC = highest_count(cD)
    lC = lowest_count(cD)
    
    print('\nLetter count: ')
    for key, value in cD.items():
        print(key, '    ', value)
    print()
    print('Letter(s) with highest count -', cD.get(hC[0]))
    for i in range(0, len(hC)):
        print(hC[i])
    print()
    print('Letter(s) with lowest count -', cD.get(lC[0]))
    for i in range(0, len(lC)):
        print(lC[i])

main()