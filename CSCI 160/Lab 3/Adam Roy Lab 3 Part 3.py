'''
Adam Roy
CSCI 160
LAB 3 PART 3
'''

#Ask for credit inputs
tcredits = int(input('How many college credits do you have so far: '))
scredits = int(input('How many college credits are you taking this semester: '))

#Calculations

if(tcredits >= 0 and tcredits <= 23):
    print('With', tcredits, 'you are a freshman')
elif(tcredits >= 24 and tcredits <= 59):
    print('With', tcredits, 'you are a sophomore')
elif(tcredits >= 60 and tcredits <= 89):
    print('With', tcredits, 'you are a junior')
elif(tcredits >= 90):
    print('With', tcredits, 'you are a senior')

acredits = scredits + tcredits

if(acredits >= 0 and acredits <= 23):
    print('With', acredits, 'you will be a freshman next semester')
elif(acredits >= 24 and acredits <= 59):
    print('With', acredits, 'you will be a sophomore next semester')
elif(acredits >= 60 and acredits <= 89):
    print('With', acredits, 'you will be a junior next semester')
elif(acredits >= 90):
    print('With', acredits, 'you will be a senior next semester')

gcred = 120

if(gcred > acredits):
    credleft = gcred - acredits
    print('You need', credleft, 'to graduate')
else:
    print('You have enough credits to graduate')
