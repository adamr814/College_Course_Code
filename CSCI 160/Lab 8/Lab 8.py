'''
Adam Roy
Lab 8
CSCI 160
'''
import os

def findMaxValue(inFile):
    maxv = -10000
    for i in range(0, len(inFile)):
        if inFile[i] > maxv:
            maxv = inFile[i]
        i += 1
    return(maxv)

def findMinValue(inFile):
    minv = 10000
    for i in range(0, len(inFile)):
        if inFile[i] < minv:
            minv = inFile[i]
        i += 1
    return(minv)  

def findFirstOccurance(theList, valueToFind):
    for i in range(0, len(theList)):
        if theList[i] == valueToFind:
            return(i)
        i += 1
    return(-1)
    
def findLastOccurance(theList, valueToFind):
    for i in range(len(theList)-1, -1, -1):
        if theList[i] == valueToFind:
            return(i)
        i += 1
    return(-1)   
    
def calcAverage(inFile):
    aveval = 0
    tval = 0
    x = 0
    while x <= len(inFile):
        for i in range(0, len(inFile)):
            tval = tval + inFile[i]
            i += 1
            x += 1
    aveval = tval / len(inFile)
    return(aveval)
    
def findNumberAboveAverage(aveval, inFile):
    aaval = 0
    for i in range(0, len(inFile)):
        if inFile[i] > aveval:
            aaval += 1
    return(aaval)
        
def findNumberBelowAverage(aveval, inFile):
    baval = 0
    for i in range(0, len(inFile)):
        if inFile[i] < aveval:
            baval += 1
    return(baval)
    
def standardDeviation(aveval, inFile):
    sdval = []
    sd = 0
    for i in range(0, len(inFile)):
        sd = (aveval - inFile[i]) ** 2
        sdval.append(sd)
    return(sdval)
        
        

def main():
    f = input('Enter a file name: ')
    if not os.path.isfile (f):
        print('\nThe input file is invalid or does not exist')
        os._exit(0)
        
    inFile = []
    f = open(f, 'r')
    lines = f.readlines()
    i = 0
    for i in range(0, len(lines)):
        x = int(lines[i].strip('\n'))
        inFile.append(x)
        i += 1
        
    maxv = findMaxValue(inFile)
    print('\nThe max value in the list is: ', maxv)
    
    minv = findMinValue(inFile)
    print('\nThe min value in the list is: ', minv)
    
    findValue = int(input('\nValue to find: '))
    focc = findFirstOccurance(inFile, findValue)
    if focc == -1:
        print('\nThe value does not exist for first occurance')
    else:
        print('\nThe first occurance of', findValue, 'was found at position', focc)
       
    locc = findLastOccurance(inFile, findValue)
    if locc == -1:
        print('\nThe value does not exist for last occurance')
    else:
        print('\nThe last occurance of', findValue, 'was found at position', locc)
        
    aveval = calcAverage(inFile)
    print('\nThe average is ', aveval)
    
    aaval = findNumberAboveAverage(aveval, inFile)
    print('\nValues above the average of', aveval, ': ', aaval)
    
    baval = findNumberBelowAverage(aveval, inFile)
    print('\nValues below the average of', aveval, ': ', baval, '\n')
    
    sdval = standardDeviation(aveval, inFile)
    x = 0
    for i in range(0, len(sdval)):
        print('Standard Deviation for position', x, 'is', sdval[i])
        x += 1
       
main()