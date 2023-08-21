def mergeSort(array, n):
    temp_array = [0]*n
    return _mergeSort(array, temp_array, 0, n-1)

def _mergeSort(array, temp_array, left, right):
    inversions = 0
    if left < right:
        mid = (left + right)//2
        inversions += _mergeSort(array, temp_array,
                                left, mid)
        inversions += _mergeSort(array, temp_array,
                                mid + 1, right)
        inversions += merge(array, temp_array, left, mid, right)
    return inversions

def merge(array, temp_array, left, mid, right):
    i = left     
    j = mid + 1  
    k = left     
    inversions = 0
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            k += 1
            i += 1
        else:
            temp_array[k] = array[j]
            inversions += (mid-i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_array[k] = array[i]
        k += 1
        i += 1
    while j <= right:
        temp_array[k] = array[j]
        k += 1
        j += 1
    for l in range(left, right + 1):
        array[l] = temp_array[l]

    return inversions

array = [95, 80, 60, 40, 20, 10, 90, 70, 50, 30]
n = len(array)
inv = mergeSort(array, n)
print('Inversions =', inv)