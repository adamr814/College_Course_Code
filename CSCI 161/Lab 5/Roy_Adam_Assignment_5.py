'''
Adam Roy
Assignment 5
CSCI 161
'''

def main():
    title = str(input('Enter a title: '))
    print('You entered: ', title)
    col1 = input('Enter the name of column 1: ')
    print('You entered: ', col1)
    col2 = input('Enter the name of column 2: ')
    print('You entered: ', col2)
    inp = 0
    liststr = []
    listint = []
    while inp != '-1':
        inp = input('Enter a data (-1 to stop input): ')
        comma = 0
        for i in range(0, len(inp)):
            if inp[i] == ',':
                comma += 1
        if comma == 1:
            string = inp.split(',')
            if string[1].isnumeric() == True:
                liststr.append(string[0])
                listint.append(string[1])
            else:
                print('\nComma not followed by an integer.\n')
        elif comma == 0:
            print('\nNo comma in string.\n') 
        elif comma > 1:
            print('\nToo many commas in string.\n') 
    print('{:^42}'.format(title))
    print('{:<20}'.format(col1), '{:>23}'.format(col2))
    for i in range(0, len(liststr)):
        print('{:<20}'.format(liststr[i]), '|', '{:>17}'.format(listint[i]))
        i += 1
        
main()