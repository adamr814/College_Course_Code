'''
Adam Roy
LAB 4
PART 3
'''

posval = 0
negval = 0
pvn = 0
nvn = 0

var = 1
val = int(input('Enter a value: '))
while(val != 0): 
    if val > 0:
        posval = posval + val
        pvn = pvn + 1
    elif val <0:
        negval = negval + val
        nvn = nvn + 1
    val = int(input('Enter a value: '))

print('Average of positive values: ', (posval / pvn))
print('Average of negative values: ', (negval / nvn))
