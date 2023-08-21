'''
Adam Roy
CSCI 160
Project 1
'''

'''
ts = total scores
tsp = total student points
tpp  = total possible points
cp = class percentage
lg = letter grade
ss = student status
ma = missed assignemt
'''

#assign variables
tsp = 0
tpp = 0
ts = 0
cp = 0
ma = 0
lg = 'Letter Grade'
#main loop
assignscore = int(input('Enter the score of your assignment (if graded): ')) #addresses possibility its early in semester
while assignscore >= 0:
    assignworth = int(input('What is the highest possible score: '))
    if assignscore == 0:
        ma += 1
    ts += 1
    tsp = tsp + assignscore
    tpp = tpp + assignworth
    assignscore = int(input('Enter the score of the next assignment: '))

#calculate percentage
cp = tsp / tpp

#calculate letter grade
if cp >= .90:
    lg = 'A'
elif (cp <= .89) and (cp >= .80):
    lg = 'B'
elif (cp <= .79) and (cp >= .70):
    lg = 'C'
elif (cp <= .69) and (cp >= .60):
    lg = 'D'
else:
    lg = 'F'

#determine if student dropped
if tsp == 0:
    ss = 'Dropped'
else:
    ss = 'Enrolled'

#print results
print()
print('Total Number of scores entered: {:>2}'.format(ts))
print()
print('Total points for the student: {:>5}'.format(tsp))
print()
print('Total possible points: {:>12}'.format(tpp))
print()
print('Class percentage: {:>21.2f}'.format(cp * 100))
print()
print('Class Letter Grade: {:>14}'.format(lg))
print()
print('Student status: {:>25}'.format(ss))
print()
print('Total missing assignments: {:>7}'.format(ma))



    
    
    
