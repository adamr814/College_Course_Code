'''
Adam Roy
CSCI 161
Assignment 11
'''

array = [22, 64, 11, 34, 25, 90, 12]

def sort(numbers): #is the user defined function that contains the algorithm
    for i in range(1, len(numbers)): #creates a loop and continues to execute until all numbers are in place
        e1 = numbers[i] #this is the element of the list that is currently being moved
        j = i - 1 #is an element that is used to temporarily switch places with other elements to move them into the correct place
        while j >= 0 and numbers[j] > e1: #goes through the list to find the correct position for the element that is selected
            numbers[j + 1] = numbers[j] #shifts the element to the left if it falls under the condition
            j -= 1
        numbers[j + 1] = e1 #places the element in the correct location
    return numbers #returns the final list
        
def main():
    print('Un-sorted List = ', end='')
    print(array)
    print()
    sl = sort(array)
    print('   Sorted List = ', end='')
    print(sl)
main()
