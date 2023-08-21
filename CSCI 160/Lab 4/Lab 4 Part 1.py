'''
Adam Roy
LAB 4
PART 1
'''

#count from 10 to 50 with each variable on a seperate line
print('Part 1')
for i in range(10, 51, 1):
    print(i)
print()

#count from 20 0 on a single line
print('Part 2')
for j in range(20, -1, -1):
    print(j, end = ' ')
print()

#count by 1/2 from 0 to 10
print('Part 2')
print('0.0')
for h in range(1 , 21, 1):
    v = 0.5 * h
    print(v)
print()

#ask for letters then count the letters
up = 0
low = 0
var = 'a'
let = input('Enter a letter: ')
while (var != 'q'):
    print("You entered '{}'".format(let))
    if let.isupper():
        up = up + 1
    else:
        low = low + 1
    let = input('Enter a letter: ')
    var = let.lower()
    


    
print('The user entered', up, 'upper case letter')
print('The user entered', low, 'lower case letter')
