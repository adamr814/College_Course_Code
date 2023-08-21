'''
Adam Roy
Lab 9
CSCI 160
'''

import os

def fillList(f):
    f = open(f, 'r')
    lines = f.readlines()    
    inFile = []
    i = 0
    for i in range(0, len(lines)):
        x = int((lines[i]).strip('\n'))
        inFile.append(x)
        i += 1 
    f.close()
    return inFile

def printList(inFile):
    pList = []
    temp = ['    ']
    for i in range(0, len(inFile)):
        pList.append(str(inFile[i]) + temp[0])   
    return pList
        
def updateList(fL):
    cList = []
    for i in range(0, len(fL)):
        cList.append(fL[i] - 5)
        i += 1
    return cList

def mergeLists(inFile, cList,):
    mList = []
    i = 0
    for i in range(0, len(inFile)):
        mList.append(inFile[i] + cList[i])
        i += 1
    return mList

def adjustList():
    aList = []
    i = 0
    for i in range(0, len(mList)):
        if mList[i] < 0:
            mList[i] == 0
        elif mList[i] > 100:
            mlist[i] == 100
        aList.append(mList[i])
        i += 1
        
def inAscendingOrder(aList):
    j = 0
    for j in range(0, len(aList) -1):
        i = 0
        for i in range(0, len(aList) -1):
            if aList[i] > aList[i + 1]:
                return False
                #temp = aList[i]
                #aList[i] = aList[i + 1]
                #aList[i + 1] = temp
            i += 1
        j += 1
    return True

def inDecendingOrder(dList):
    j = 0
    for j in range(0, len(dList) -1):
        i = 0
        for i in range(0, len(dList) -1):
            if dList[i] < dList[i + 1]:
                return False
                #temp = aList[i]
                #aList[i] = aList[i + 1]
                #aList[i + 1] = temp
            i += 1
        j += 1
    return True    

def matchingValues(mvList):
    highLimit = 50
    lowLimit = 5
    mList = []
    i = 0
    for i in range(0, len(mvList) -1):
        if mvList[i] < highLimit and mvList[i] > lowLimit:
            mList.append(mvList[i])                
        i += 1   
    return mList

def main():
    f = input('Enter a file name: ')
    if not os.path.isfile (f):
        print('\nThe input file is invalid or does not exist')
        os._exit(0)
    
    fL = fillList(f)
    
    pL = printList(fL)
    print('List inputed:\n', pL, '\n')

    cL = updateList(fL)
    
    mL = mergeLists(fL, cL)
    
    aL = inAscendingOrder(fL)
    print(aL)
    
    dL = inDecendingOrder(fL)
    print(dL)
    
    mvL = matchingValues(fL)
    print(mvL)
    
main()
