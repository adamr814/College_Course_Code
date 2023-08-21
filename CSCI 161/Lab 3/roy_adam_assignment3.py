'''
Adam Roy
Assignment 3 Part 1
CSCI 161
'''

import os

def inpMm():
    numbers = []
    minval = int(input('\nEnter the minimum value: '))
    maxval = int(input('\nEnter the maximum value: '))
    while minval >= maxval:
        maxval = int(input('\nPlease enter a new maximum value: '))
    return minval, maxval

def printOdd(x, y):
    i = x
    print('\nListed odd numbers')
    while i in range(x, y + 1):
        if(i % 2 != 0): 
            print(i, end=' ')    
        i += 1
    print()
        
def printPrime(x, y):
    print('\nListed prime numbers')
    for num in range(x, y + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end= ' ')
    print()
        
def printTwo(x, y):
    #num = x
    print('\nRange by two')
    n = 2
    for num in range(x, y + 1, n):
        print(num, end= ' ')
    print()

def printTwoNotThree(x, y):
    #num = x
    print('\nRange by two but not divisible by three')
    n = 2
    for num in range(x, y + 1, n):
        if(num % 3 != 0):
            print(num, end= ' ')
        else:
            continue
    print()
    
def main():   
    x, y = inpMm()
    printOdd(x, y)
    printPrime(x, y)
    printTwo(x, y)
    printTwoNotThree(x, y) 
main()