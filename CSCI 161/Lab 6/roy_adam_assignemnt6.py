'''
Adam Roy
Assignment 6
CSCI 161
'''
import os

def printMenu():
    print('''
Menu
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
''')
    option = input("Choose an option: ")
    return option

def outputRoster():
    playerList.sort()
    print("ROSTER")
    for players in playerList:
        print("Jersey number: ", players, "Rating: ", playerDict[players])
        
def addPlayer():
    jersey = int(input("Enter a new player's jersey number: "))
    rating = int(input("Enter the player's rating: "))
    playerDict[jersey] = rating
    playerList.append(jersey)
    playerList.sort()
    
def deletePlayer():
    deleteJersey = int(input("Enter a jersey number: "))
    playerDict.pop(deleteJersey)
    playerList.remove(deleteJersey)
    
def updateRating():
    jersey = int(input("Enter a jersey number: "))
    rating = int(input("Enter a new rating for player: "))
    playerDict[jersey] = rating    

def outputAboveRating():
    aboveRating = int(input("Enter a rating: "))
    print("ABOVE ", aboveRating)
    for players in playerList:
        if playerDict[players] > aboveRating:
            print("Jersey number: ", players, "Rating: ", playerDict[players])
x = 1
playerDict = {}
playerList = []
while x <= 5:
    print("Enter player", x, "'s jersey number(0-99): ")
    playerJersey = int(input())
    print("Enter player", x, "'s rating(1-9): ")
    playerRating = int(input())
    playerDict[playerJersey] = playerRating
    playerList.append(playerJersey)
    x += 1
playerList.sort()
for players in playerList:
    print("Jersey number: ", players, "Rating: ", playerDict[players])
option = printMenu()
option = option.lower()
while option != 'q':
    if option == 'o':
        outputRoster()
    if option == 'a':
        addPlayer()
    if option == 'd':
        deletePlayer()
    if option == 'u':
        updateRating()
    if option == 'r':
        outputAboveRating()
    option = printMenu()
    option = option.lower()
    

    
    
