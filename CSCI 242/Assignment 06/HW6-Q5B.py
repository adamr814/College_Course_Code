def mode(array):
    mxCount = (0, 0)
    for num in array:
        occ = array.count(num)
        if occ > mxCount[0]:
            mxCount = (occ, num)
    return mxCount

array = [90, 70, 60, 40, 20, 50, 60, 90, 20, 30, 90, 70, 50, 30, 90]
count = mode(array)
print(count)