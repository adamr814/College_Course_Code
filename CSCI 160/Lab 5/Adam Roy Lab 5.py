'''
Adam Roy
CSCI 160
LAB 5
'''
import math
totalCredits = 0
honorPoints = 0
classesAttempted = 0
classa = 0
classp = 0
creditsPassed = 0
classes = input('Enter a class: ')
while classes != '':
    credit = int(input('Enter the number of credits: '))
    grade = input('Enter your grade: ')
    print()

    letter = grade.lower()
    if letter == 'a':
        grade = 4
    elif letter == 'b':
        grade = 3
    elif letter == 'c':
        grade = 2
    elif letter == 'd':
        grade = 1
    elif letter == 'f':
        grade = 0
    classa = classa + 1
    totalCredits = totalCredits + credit
    honorPoints = honorPoints + (credit * grade)
    if grade != 0:
        classp = classp + 1
        creditsPassed = creditsPassed + credit
    classes = input('Enter the next class: ')
    
gpa = honorPoints / totalCredits
    
print('GPA: {:>19}'.format(round(gpa, 3)))
print('Credits attempted {:>6}'.format(totalCredits))
print('Credits passed {:>9}'.format(creditsPassed))
print('Classes attempted {:>6}'.format(classa))
print('Classes passed {:>9}'.format(classp))

