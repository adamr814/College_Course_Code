'''

Adam Roy
CSCI 160
LAB 2
PART 2

'''

#Convert from seconds
#Input value for seconds

sec = int(input('Enter time in seconds '))

#Do calculations

hour = sec // 3600
sec = (sec - 3600 * hour)

minute = sec // 60
sec = (sec - 60 * minute)



print('This is',hour, 'hours,', minute, 'minutes and', sec, 'seconds.')
