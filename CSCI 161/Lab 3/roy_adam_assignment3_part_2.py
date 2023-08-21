'''
Adam Roy
Assignment 3 Part 2
CSCI 161
'''

import os

def assignList():
    list = [3, 1, 4, 15, 926, 5, 35, 8, 97, 93]
    return list

def findSum(list):
    i = 0
    val = 0
    for i in range(len(list)):
        if list[i] != 5:
            val = val + list[i]
        i += 1
    return val
    
def findIndex(list):
    i = 0
    index = None
    for i in range(len(list)):
        if list[i] == 5:
            index = i - 1
    return index

def main():
    aL = assignList()
    fS = findSum(aL)
    fI = findIndex(aL)
    
    print(aL)
    print('\nProduct of all values before index: ', fS)
    print('\nIndex value: ', fI)
main()