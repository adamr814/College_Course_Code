x = float(input('Enter first value: '))
y = float(input('Enter second value: '))

if not x <= 0 and not y <= 0:
    sum = x + y
    print('The answer is: ', sum)
else:
    print('Negative variables are not accepted')
