'''
Adam Roy
Project 2
CSCI 160
'''

def createList(inp):
    List = []
    i = 0
    for i in range(0, inp):
        List.append(-1)
        i += 1
    return List

def setScore(labScore, cL):
    lS = labScore.split()
    str1 = lS[0]
    str2 = lS[1]
    num1 = int(str1)
    num2 = int(str2)
    
    cL[(num1 - 1)] = num2
    return cL

def getScore(cL):
    i = 0
    cLcopy = []
    for i in range(0, len(cL)):
        if cL[i] == -1:
            cL[i] = ''
            cLcopy.append(cL[i])            
        else:
            cLcopy.append(cL[i])
        i += 1
    return cLcopy

def totalPoints(labScore):
    lS = labScore.split()
    str2 = lS[1]
    num2 = int(str2)
    total = 0
    total += num2
    return total
    
def totalPossible(cL):
    tpp = len(cL) * 10
    return tpp
    
def getLabAverage(tpp, times):
    gla = tpp / times
    return gla

def printScores(gS, tP, tPo, gLA, cL):
    print('In Class Lab Scores')
    print('Lab    Score')
    j = 0
    for j in range(0, len(cL)):
        print(' {:<2}'.format((j + 1)), '{:>8}'.format(gS[j]))
        j += 1
    print('Total Points:', tP)
    print('Total Points Possible:', tPo)
    print('Lab Average:', gLA)

def main():
    inp = int(input('Enter number of labs: '))
    cL = createList(inp)
    times = 0
    i = 0
    for i in range(0, len(cL)):
        labScore = input('\nEnter Lab Number And Score ## ##: ')
        times += 1
        if labScore == '':
            break
        sS = setScore(labScore, cL)
        tempP = totalPoints(labScore)
        i += 1
    gS = getScore(cL)
    tP = tempP
    tPo = totalPossible(cL)
    gLA = getLabAverage(tPo, times)
    pSc = printScores(gS, tP, tPo, gLA, cL)
       
main()
