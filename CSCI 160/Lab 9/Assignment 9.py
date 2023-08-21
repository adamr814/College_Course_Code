'''
Adam Roy
Assignment 9
CSCI 160
'''
import os

def time_splitter(inFile):
    time = []
    i = 0
    for i in range(0, len(inFile)):
        x = (inFile[1].split(':'))
        time.append(x)
        i += 1
       
def time_adder(inFile, time_splitter):
    minutes = 0
    seconds = 0
    for i in range(0, len(inFile)):
        minutes = minutes + time[0]
        seconds = seconds + time[1]
        i += 1
    while seconds >= 60:
        seconds - 60
        minutes + 1

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
        x = (lines[i].strip('\n').split('|'))
        inFile.append(x)
        i += 1
    left = time_adder(inFile, time_splitter)
    i = 0
    for i in range(0, len(inFile)):
        allValues = str(inFile[0])
        x = str(left)
        print('{:<12}'.format(x), )
    
    right = time_adder(inFile, time_splitter)
    print ('{:>6}'.format(minutes, seconds))
    
    main()