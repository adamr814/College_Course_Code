'''
Adam Roy
CSCI 160
LAB 3 PART 1
'''

#Enter a floating point value
fval = float(input('Enter a number: '))
a = fval
b = fval
d = fval
e = fval
f = fval
ival = int(fval)
c = ival

#Determine if the value has a fractional part
if((a % 1) != 0):
    print(fval, 'Has a fractional part')
else:
    print(ival, 'Does not have a fractional part')

#Determine if the value is a multiple of 6
if((b % 6) != 0):
    print(fval, 'is not a multiple of 6')
else:
    print(ival, 'is a multiple of 6')

#Determine if the value is even or odd
if((c % 2) != 0):
    print(ival, 'is an odd number')
else:
    print(ival, 'is an even number')

#Determine if the value is positive, negative or zero
if(d == 0):
    print(ival, 'is zero')
elif(d < 0):
    print(fval, 'is negative')
elif(d > 0):
    print(fval, 'is positive')

#Determine if the value is between two values
if(e >= 2020 and e <= 2029):
    print(ival, 'is within the range of 2020 and 2029')
else:
    print(ival, 'is not within the range of 2020 and 2029')

#Determine if the value is in the 100's
if(f >= 100 and f <= 199):
    print(ival, 'is within the 100\'s')
else:
    print(ival, 'is not within the 100\'s')

#End of program
