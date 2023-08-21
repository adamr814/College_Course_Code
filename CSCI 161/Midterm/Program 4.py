'''
Adam Roy
CSCI 161
MIDTERM Program 4
'''

l = []
i = 0
for i in range(0, 5):
    inp = input("Enter a name: ")
    l.append(inp)
    i += 1
    
l.sort()
j = 0
print("\nSorted List:\n")
for j in range(0, 5):
    print(l[j])