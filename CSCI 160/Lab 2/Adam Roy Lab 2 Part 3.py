'''

Adam Roy
CSCI 160
LAB 2
PART 3

'''

#Convert money

#Input quantity of quarters
qt = int(input('Enter ammount of quarters: '))
#Input quantity of dimes
dm = int(input('Enter ammount of dimes: '))
#Input quantity of nickles
ns = int(input('Enter ammount of nickles: '))
#Input quantity of pennies
ps = int(input('Enter ammount of pennies: '))

#Calculations
cents = ((qt * 25) + (dm * 10) + (ns * 5) + (ps)) / 100

print('This is equal to ${}'.format(cents))
    
