temp = int(input('Enter a Temperature in Celsius: '))
while temp != 999: 
    if temp <= -25:
        print(temp,'= Extremely Cold')
    elif (temp >= -24) and (temp <= 10):
        print(temp, '= Cold')
    elif (temp >= 11) and (temp <= 32):
        print(temp, '= Warm')
    elif (temp >= 33):
        print(temp, '= Extemely Hot')
    dif = 20 - temp
    diff = abs(dif)
    print('The differance from average 20 is', diff)
    temp = int(input('Enter a Temperature in Celsius: '))
    
