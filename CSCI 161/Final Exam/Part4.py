'''
Adam Roy
FINAL PROGRAM Part 4
CSCI 161
'''
#ver 1.8
class Node:
    def __init__(self,data):
        self.data = data
        self.point = None
def is_palindrome(head):
    s = head
    stack = []
    ispalin = True
    while s != None:
        stack.append(s.data)
        s = s.point
    while head != None:
        i = stack.pop()
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break
        head = head.point
    return ispalin
List1 = [1,2,2,1]
List2 = [1,2,3,4,5]
a = Node(1)
b = Node(2)
c = Node(2)
d = Node(1)
a.point = b
b.point = c
c.point = d
d.point = None
result = is_palindrome(a)
print(List1)
NL1 = List1[::-1]
print(NL1)
print('Is palindrome: ', result)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.point = b
b.point = c
c.point = d
d.point = e
e.point = None
result = is_palindrome(a)
print()
print(List2)
NL2 = List2[::-1]
print(NL2)
print('Is palindrome: ', result)