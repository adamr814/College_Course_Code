'''
Adam Roy
LAB 6
PART 2
'''

import os

f = input('Enter an input file: ')

if not os.path.isfile (f):
    print('\nThe input file is invalid or does not exist')
    os._exit(0)

print('Selected File: ', f)
inFile = open (f, 'r')
numList = []
numList = inFile.readlines()
for i in range(len(numList)):
    numList[i] = int(numList[i].replace('\n', ''))
    i += 1

for i in range(len(numList)-1):
    if numList[i] > numList[i + 1]:
        x = numList[i + 1]
        numList[i] = numList[i + 1]
        numList[i] = x
        i += 1
lengthlist = len(numList) -1
  
#find the minimum value
min_val = numList[0]
print('Minimum value: ', min_val)

#find the maximum value
max_val = numList[lengthlist]
print('Maximum value: ', max_val)

#if any values are 100
for i in range(len(numList)):
    if numList[i] == 100:
        print('The value 100 is on line: ', (i + 1))
    i += 1
    
#if any values are 0
for i in range(len(numList)):
    if numList[i] == 0:
        print('The value 0 is on line: ', (i + 1))
    i += 1

#The average of all of lines in the file
total = 0
for i in range(len(numList)):
    total += numList[i]
    i += 1
ave = total / len(numList)
print('The average is: {:.4f}'.format(ave))

#total number of values
print('The number of values is: ', len(numList))

#number of values above and below 75
gtot = 0
ltot = 0
for i in range(len(numList)):
    if numList[i] >= 75:
        gtot += 1
    else:
        ltot += 1
    i += 1
print('The number of values above 75 is: ', gtot)
print('The number of values less than 75 is: ', ltot)

#last section is causing issues
#end of program




