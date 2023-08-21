'''
Adam Roy
CSCI 161
Assignment 2
'''
import os

def inputValue():
    inp = input('Enter a Number: ')
    
    if inp.isnumeric():
        val = float(inp)
        return val
    else:
        print('\nThe variable is not a number or in the proper format')
        os._exit(0)

def isWholeNum(val):
    if val - int(val) == 0:
        return "Yes"
    else:
        return "No"

def isMultOf7(val):
    if val % 7 == 0:
        return "Yes"
    else:
        return "No"
    
def posNegZero(val):
    if val > 0:
        return "Positive"
    elif val == 0:
        return "Zero"
    elif val < 0:
        return "Negative"
    
def isInRange(val):
    if val >= 2011 and val <= 2021:
        return "in range"
    else:
        return "not in range"

def isThousands(val):
    if val >= 100 and val <= 9999:
        return "in range"
    else:
        return "not in range"

def inputValue2():
    inp2 = input('\nEnter Number Two: ')
    
    if inp2.isnumeric():
        val2 = float(inp2)
        return val2
    else:
        print('\nThe variable is not a number or in the proper format')
        os._exit(0)    

def smallVal(val, val2):
    if val > val2:
        return "Value 1 is greater"
    elif val == val2:
        return "Values are equal"
    elif val < val2:
        return "Value 2 is greater"
    
def valMultiple(val, val2):
    if val % val2 == 0:
        return "Value 2 is a multiple of Value 1"
    else:
        return "Value 2 is NOT a multiple of Value 1"
    
def val2Multiple(val, val2):
    if val2 % val == 0:
        return "Value 1 is a multiple of Value 2"
    else:
        return "Value 1 is NOT a multiple of Value 2"
    
def main():
    iV = inputValue()
    iWN = isWholeNum(iV)
    iMO7 = isMultOf7(iV)
    pNZ = posNegZero(iV)
    iIR = isInRange(iV)
    iT = isThousands(iV)
    
    print('\nInput is whole number: ', iWN)
    print('Input is a multiple of 7: ', iMO7)
    print('Input is: ',pNZ)
    print('Input is between 2011 and 2021: ', iIR)
    print('Input is 4 digits: ', iT)
    
    iV2 = inputValue2()
    sV = smallVal(iV, iV2)
    vM = valMultiple(iV, iV2)
    v2M = val2Multiple(iV, iV2)
    
    print('\nInput 1 vs. Input 2: ', sV)
    print(vM)
    print(v2M)
    
    
main()