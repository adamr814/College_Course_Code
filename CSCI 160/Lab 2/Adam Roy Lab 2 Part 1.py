'''

Adam Roy
CSCI 160
LAB 2
PART 1

'''

#Propmpt user to enter three intagers for hours, minutes and seconds

hours = int (input('Enter Hours: '))
minutes = int (input('Enter Minutes: '))
seconds = int (input('Enter Seconds: '))

htm = (hours * 60)
mfh = (minutes + htm)
mts = (mfh * 60)
print(mts)
