'''
Adam Roy
CSCI 160
LAB 7
PART 1
'''

import math
intValue = 0

def square (num_squared):
    return num_squared * num_squared
num_squared = square(intValue)

    #This section is used to calculate the square of the number entered

def summation (summation_num):
    x = 1
    while x <= intValue:
        summation_num = summation_num + x
        x += 1
    return summation_num
summation_num = summation(intValue)
    #This section is used to calculate the summation of the number entered

def sumOfSquare (num_sos):
    while sumx <= intValue:
        sumy = sumx ** 2
        sos = sos + sumy
        sumx += 1
    return num_sos
num_sos = sumOfSquare(intValue)
#This section is used to calculate the sum of every square of each value until the input number is reached
        
def factorial (factorial_num):
    fact = 1
    for i in range(1, intValue + 1):
        fact = fact * i
    return factorial_num
factorial_num = factorial(intValue)
#This section is used to calculate the factorial of the input value

def distance_val (num_x1, num_x2, num_y1, num_y2):
    xa = input('Enter point x1 ')
    ya = input('Enter point y1 ')
    xb = input('Enter point x2 ')
    yb = input('Enter point y2 ')
    return num_x1, num_x2, num_y1, num_y2
num_x1 = xa(distance_val)
num_x2 = xb(distance_val)
num_y1 = ya(distance_val)
num_y2 = yb(distance_val)
#This section is used to input the values for def distance

def distance (dist_nums):  
    dist = sqrt(((num_x2 - num_x1)**2) + ((num_y2 - num_y1)**2))
    return dist_nums
dist_nums = distance(intValue)
#This section is used to calculate the distance between the points given in distance_val

def isOdd (num_odd):
    num = main(intValue)
    if (num % 2) != 0:
        num_odd = 'True'
    else:
        num_odd = 'False'
    return num_odd
num_odd = isOdd(intValue)
#This section determines if the value is odd

def isEven (num_even):
    num = main(intValue)
    if (num % 2) == 0:
        num_even = 'True'
    else:
        num_even = 'False'
    return num_even
num_even = isEven(intValue)
#This section determines if the value is even

def main ():
    intValue = int(input('Enter a number: '))
    print(intValue, 'squared is', num_squared)
    print('The summation of', intValue, 'is', summation_num)
    print('The sum of squares for', intValue, 'is', num_sos)
    print('The factorial of', intValue, 'is', factorial_num)
    print('The distance between the points given is', dist_nums)
    print(intValue, 'is odd', num_odd)
    print(intValue, 'is even', num_even)

main()
