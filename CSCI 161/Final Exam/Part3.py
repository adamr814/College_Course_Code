'''
Adam Roy
FINAL PROGRAM Part 3
CSCI 161
'''
#ver 1.1

List = [9,2,4,3,2,6,6,9]
numbers = []
count = {}
for x in List:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
        numbers.append(x)
for x in numbers:
    if count[x] == 1:
        print(x)
        break