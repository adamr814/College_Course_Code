'''
Adam Roy
Lab 10
CSCI 160
'''

import os
import random

def createDict(f):
    f = open(f, 'r')
    i = 0
    lines = f.readlines()
    words = {}
    for i in range(0, len(lines)):
        x = lines[i]
        words[i] = lines[i].strip('\n')
        i += 1
    f.close()
    return words

def chooseDifficulty():
    lives = 0
    dif = input("choose a difficulty, 'easy' 'medium' or 'hard': ")
    while lives == 0:
        if dif == 'easy':
            lives = 9
        elif dif == 'medium':
            lives = 7
        elif dif == 'hard':
            lives = 5
        else:
            print('Invalid difficulty selected')
            dif = input("choose a difficulty, 'easy' 'medium' or 'hard'")
    return lives
            
def chooseRandWord(words):
    x = random.randint(0, 19)
    currentWord = words[x]
    return currentWord

def splitWord(currentW):
    res = []
    res[:] = currentW
    return res

def create_empty_char(word):
    i = 0
    eC = word
    for i in range(0, len(word)):
        eC(i) = '*'
        i += 1
    return eC

def userGuess():
    letterGuess = str(input('Your Guess? '))      
    return letterGuess

def guesses(letterGuess):
    guessedLetters = []
    guessedLetters.append(letterGuess)
    return guessedLetters
    
def main():
    f = 'words.txt'
    if not os.path.isfile (f):
        print('\nInput file is missing')
        os._exit(0)
    
    cD = createDict(f)
    cDiff = chooseDifficulty()
    cRW = chooseRandWord(cD)
    sW = splitWord(cRW)
    cEC = create_empty_char(cRW)
    gL = userGuess()
    g = guesses(gL)
    
    print(sW)
    while cDiff > 0:
        if cEC == sW:
            print('You win!')
            #break
        else:
            print('Word: ', cEC)
            print(gL)
            print('Previous Guesses: ', g)
            i = 0
            for i in range(0, len(sW)):
                if gL in cRW:
                    print(gL, 'is in the word,', cDiff, 'guesses remaining')
                    cEC[i].replace(sW[i])
                else:
                    cDiff -= 1
                    print(gL, 'is not in the word,', cDiff, 'guesses remaining')
                userGuess()
    print('Sorry you ran out of guesses')
    #ng = input('Would you like to play again? Y/N')
    #if ng == Y

main()