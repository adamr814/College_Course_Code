temp = int(input('Enter a Temperature in Celsius: '))
while temp != 999: 
    degf = temp * 1.8 + 32
    if temp <= -25:
        print(degf,'= Extremely Cold')
    elif (temp >= -24) and (temp <= 10):
        print(degf, '= Cold')
    elif (temp >= 11) and (temp <= 32):
        print(degf, '= Warm')
    elif (temp >= 33):
        print(degf, '= Extemely Hot')
    dif = 20 - temp
    diff = abs(dif)
    print('The differance from average 20 is', diff)
    temp = int(input('Enter a Temperature in Celsius: '))
    
