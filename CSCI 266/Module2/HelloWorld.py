'''
Adam Roy
CSCI 266
Module 2

Hello World Python Script
'''

def outputToScreen(textToPrint):
    print("*******************")
    print("%15s" %textToPrint)
    print("*******************")

def main():
    textToPrint = "Hello World"
    outputToScreen(textToPrint)

main()