'''
Adam Roy
Lab 11
CSCI 160
'''
import os
d = -1
def open_file(f):
    d = {}
    f = open(f, 'r')
    for line in f:
        x = line.strip('\n')
        (val, key) = x.split(':')
        d[(key)] = val
    f.close()
    return d

def new_entry(d):
    # name input
    val = input('Name to add: ')
    print('Date for', val, ': ', end= '')
    # date input
    key = int(input())
    d[(key)] = val
    return d

def search_by_date(d):
    inp = int(input('\nEnter a date: '))
    while inp != 0:    
        for key, value in d.items():
            if inp == value:
                return key
            inp = int(input('\nEnter a date: '))
        return 'Date does not exist'
    
def display_dates(d):
    print(d)
        

def main():
    mC = showMenu()
    if mC == 1:
        f = str(input('\nEnter a file name: '))
        if not os.path.isfile (f):
            print('\nInput file is invalid or does not exist')
            os._exit(0)         
        oF = open_file(f)
        main()
    elif mC == 2:
        nE = new_entry(oF)
        d = nE
        main()
    elif mC == 3:
        sBD = search_by_date(oF)
        print("Birthday's: ", sBD)
        main()
    elif mC == 4:
        dD = display_dates(d)
        print(dD)
        main()
    elif mC == 5:
        os._exit(0)
        
        
        
def printMenuChoices():
    print ("What would you like to do?")
    print (" 1. Open a data file")
    print (" 2. Add new name")
    print (" 3. Search by date")
    print (" 4. Display all birthdays for the month")
    print (" 5. Exit program")
    print ()

def showMenu ():
    printMenuChoices()
    menuChoice = int (input ("Your choice? "))
    while menuChoice < 1 or menuChoice > 5:
        print ("Please enter a valid choice (1-5)")
        print ()
        if menuChoice < 1 or menuChoice > 5:
            menuChoice = int ( input ("Your choice? "))
    return menuChoice
option = showMenu()
#I touched something and it broke the entire program
main()