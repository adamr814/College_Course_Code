'''
Adam Roy
CSCI 160
LAB 3 PART 2
'''

#Enter a input number
num = int(input('Please enter a value: '))

#Variable check
if(num < 20 or num > 99):
    print('The number is not within the valid range')
else:
    #Computations of tens place
    if((num // 10) == 2):
        string = 'twenty'
    elif((num // 10) == 3):
        string = 'thirty'
    elif((num // 10) == 4):
        string = 'forty'
    elif((num // 10) == 5):
        string = 'fifty'
    elif((num // 10) == 6):
        string = 'sixty'
    elif((num // 10) == 7):
        string = 'seventy'
    elif((num // 10) == 8):
        string = 'eighty'
    elif((num // 10) == 9):
        string = 'ninety'

    #Computations of ones place
    if((num % 10) == 1):
        string += ' one'
    elif((num % 10) == 2):
        string += ' two'
    elif((num % 10) == 3):
        string += ' three'
    elif((num % 10) == 4):
        string += ' four'
    elif((num % 10) == 5):
        string += ' five'
    elif((num % 10) == 6):
        string += ' six'
    elif((num % 10) == 7):
        string += ' seven'
    elif((num % 10) == 8):
        string += ' eight'
    elif((num % 10) == 9):
        string += ' nine'

    #Print number
    print('The number is', string)

    #End of program
