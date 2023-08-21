def mergeSort(array, n):
    temp_array = [0]*n
    return _mergeSort(array, temp_array, 0, n-1)

def _mergeSort(array, temp_array, left, right):
    if left < right:
        mid = (left + right)//2
        _mergeSort(array, temp_array, left, mid)
        _mergeSort(array, temp_array, mid + 1, right)
        merge(array, temp_array, left, mid, right)
    return temp_array

def merge(array, temp_array, left, mid, right):
    i = left     
    j = mid + 1  
    k = left     
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            k += 1
            i += 1
        else:
            temp_array[k] = array[j]
            (mid-i + 1)
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

    return array

array = [35, 65, 85, 25, 55, 15, 90, 40, 10, 60, 80, 70, 50, 20, 30]
n = len(array)
a = mergeSort(array, n)
print(a)