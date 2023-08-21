'''
Adam Roy
FINAL PROGRAM Part 2
CSCI 161
'''
#ver 1.2 Using Bubble Sort Method

dictionary = {2:64, 1:69, 4:23, 5:65, 6:34, 3:76}
dictkey_list = dictionary.keys()
key_list = []
key_list.extend(dictkey_list)
print(key_list)
i = 0
for i in range(len(key_list)-1,0,-1):
    for j in range(i):
        if key_list[j] > key_list[j+1]:
            temp = key_list[j]
            key_list[j] = key_list[j+1]
            key_list[j+1] = temp
sorteddict = {}
i = 0
for i in range(0, len(key_list)):
    sorteddict[key_list[i]] = dictionary.get(key_list[i])
    i += 1
print(sorteddict)
            