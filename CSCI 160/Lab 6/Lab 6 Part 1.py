'''
Adam Roy
LAB 6
PART 1
'''

#open input file
f = open(input('Enter an output file: '),'w')
#f.open('w')

if f == None:
    os.exit(0)
    
f.write('Entered Scores\n')

#ask for test scores
score = str(input('Enter test scores: '))
while score != '-1':
    f.write('{:>6}\n'.format(score))
    score = str(input('Enter next score: '))

f.write('\nEnd of file')
f.close()
