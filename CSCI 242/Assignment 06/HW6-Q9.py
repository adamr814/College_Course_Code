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
        
array = [35, 65, 85, 25, 55, 15, 90, 40, 10, 60, 80, 70, 50, 20, 30]
quicksort(array)
print(array)
        
