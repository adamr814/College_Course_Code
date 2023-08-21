'''
Adam Roy
LAB 4
PART 4
'''

v = int(input('Enter a number between 1 and 10: '))
if (v > 10) or (v < 1):
    print('Invalid Input')
else:
    print()
    print('Multipliction table for', v)
    print()
    x = 1
    while x <= 10:
#       print({:<10}, '*', {:<10}, '=', (x * v).format(x, v))        
        print(x, '*', v, '=', (x * v))
        x = x + 1
        
