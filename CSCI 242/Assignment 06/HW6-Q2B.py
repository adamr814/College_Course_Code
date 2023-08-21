def partition(a, low, high):
    i = low - 1
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quicksort(a, low = 0, high = None):
    if high == None:
        high = len(a) - 1
    if low < high:
        p_idx = partition(a, low, high)
        quicksort(a, low, p_idx - 1)
        quicksort(a, p_idx+1, high)
        
a = []
array = ['G', 'B', 'R', 'G', 'R', 'B', 'G', 'B', 'R', 'B', 'G', 'R', 'G', 'R', 'B']
for element in array:
    if element == 'R':
        a.append(1)
    if element == 'G':
        a.append(2)
    if element == 'B':
        a.append(0)
quicksort(a)
S = []
for element in a:
    if element == 1:
        S.append('R')
    if element == 2:
        S.append('G')
    if element == 0:
        S.append('B')
print(S)
        
