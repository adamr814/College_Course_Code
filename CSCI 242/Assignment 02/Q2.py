class Node:
    left = right = None

    def __init__(self, data):
        self.data = data

def isRoot(root, key):
    if key == root.data:
        print('9) Is root: True')
    else:
        print('9) Is root: False')
        
def isExternal(root, key):
    root.data == key
    if root.left == None:
        print('8) Node is external')
    else:
        print('8) Node is not external')

#def rangeQuery(root, k1, k2):
    #if root is None:
        #return
    #if k1 < root.data:
        #rangeQuery(root.left, k1, k2)
    #if k1 <= root.data and k2 >= root.data:
        #print(root.data)
    #if k2 > root.data:
        #rangeQuery(root.data, k1, k2)

def predecessor(root, dict, key):
    if root is None:
        return
    if key == root.data:
        if root.left == None:
            print('5) Predecessor is None')
        else:
            print('5) Predecessor is', dict[root.data])
    if key < root.data:
        return predecessor(root.left, dict, key)
    if key > root.data:
        return predecessor(root.right, dict, key)

def successor(root, dict, key):
    if root is None:
        return
    if key == root.data:
        if root.right == None:
            print('4) Successor is None')
        else:
            print('4) Successor is', dict[root.data])
    if key < root.data:
        return successor(root.left, dict, key)
    if key > root.data:
        return successor(root.right, dict, key)   

def search(root, dict, key):
    if root is None:
        return None
    if key == root.data:
        print('3)', dict[root.data])
    if key < root.data:
        return search(root.left, dict, key)
    if key > root.data:
        return search(root.right, dict, key)

def pRoot(root, dict):
    if root is None:
        return
    print('')
    print('2)', dict[root.data])

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
    
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root


if __name__ == '__main__':

    keys = [25, 35, 45, 20, 30, 5, 55, 43, 22, 6, 8, 40]
    dict = {25:'C', 35:'G', 45:'B', 20:'P', 30:'Q', 5:'Z', 55:'L', 43:'F', 22:'A', 6:'U', 8:'N', 40:'R'}
    root = constructBST(keys)
    inorder(root)
    pRoot(root, dict)
    key = 45
    search(root, dict, key)
    key = 8
    successor(root, dict, key)
    key = 35
    successor(root, dict, key)
    key = 20
    predecessor(root, dict, key)
    key = 40
    predecessor(root, dict, key)
    #k1 = 25
    #k2 = 45
    #rangeQuery(root, k1, k2)
    key = 40
    isExternal(root, key)
    key = 25
    isRoot(root, key)
    
    