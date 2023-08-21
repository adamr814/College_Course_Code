class HashTable:
    def __init__(self):
        self.MAX = 11
        self.arr = [[] for i in range(self.MAX)]
        self.r = 0
        
    def get_hash(self, key):
        return (2 * key + 5) % 11
    
    def delitem(self, key):
        h = (self.get_hash(key) - self.r)
        for i in range(0, len(self.arr)-1):
            if self.arr[h] == [key]:
                self.arr[h].remove(key)
                self.r += 1
                self.shiftitems()
                break
            if self.arr[h] != [key]:
                if h <= 10:
                    h += 1
                else:
                    h == 0
                
    def shiftitems(self):
        self.arr.remove([])
        self.arr.append([])
            
    
    def setitem(self, key):
        h = self.get_hash(key)
        for i in range(0, len(self.arr)):
            if self.arr[h] == []:
                self.arr[h].clear()
                self.arr[h].append(key)
                break
            elif self.arr[h] != []:
                h += 1
            elif self.arr[h] != [] and self.arr[h] >= 11:
                h == 0
                i == 0
            else:
                print("No open spots in table")
            
t = HashTable()
t.setitem(3)
t.setitem(14)
t.setitem(18)
t.setitem(37)
t.setitem(9)
t.setitem(92)
t.setitem(21)
t.setitem(86)
t.setitem(11)
print(t.arr)
t.delitem(3)
print(t.arr)
t.delitem(14)
print(t.arr)
t.delitem(18)
print(t.arr)
t.delitem(37)
print(t.arr)
t.delitem(9)
print(t.arr)
t.delitem(92)
print(t.arr)
t.delitem(21)
print(t.arr)
t.delitem(86)
print(t.arr)
t.delitem(11)
print(t.arr)