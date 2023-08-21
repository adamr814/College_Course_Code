def max_heapify(A,k):
    l = leftChild(k)
    r = rightChild(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)
        
def min_heapify(A,k):
    l = leftChild(k)
    r = rightChild(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def leftChild(k):
    return 2 * k + 1

def rightChild(k):
    return 2 * k + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)

def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)


A = [2, 5, 16, 4, 10, 23, 39, 18, 26, 15]
build_max_heap(A)
print(A)
A = [2, 5, 16, 4, 10, 23, 39, 18, 26, 15]
build_min_heap(A)
print(A)