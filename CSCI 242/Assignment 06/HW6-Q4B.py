def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] >= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kLargest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return kLargest(arr, l, index - 1, k)
        return kLargest(arr, index + 1, r, k - index + l - 1)
    print("Index out of bound")
    
arr = [90, 70, 60, 40, 20, 50, 60, 90, 20, 30, 90, 70, 50, 30, 90]
n = len(arr)
k = n//2
print("Median element is ", kLargest(arr, 0, n - 1, k))
k = 1
print("1st largest element is ", kLargest(arr, 0, n - 1, k))
k = 3
print("3rd largest element is ", kLargest(arr, 0, n - 1, k))
k = 5
print("5th largest element is ", kLargest(arr, 0, n - 1, k))
k = 10
print("10th largest element is ", kLargest(arr, 0, n - 1, k))
k = 13
print("13th largest element is ", kLargest(arr, 0, n - 1, k))
k = 15
print("15th largest element is ", kLargest(arr, 0, n - 1, k))