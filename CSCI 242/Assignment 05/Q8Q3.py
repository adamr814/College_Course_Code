class HashTable:
    def __init__(self):
        self.MAX = 11
        self.arr = [[None] for i in range(self.MAX)]
        
    def get_hash(self, key):
        return (2 * key + 5) % 11
    
    def delitem(self, key):
        h = self.get_hash(key)
        for i in range(0, len(self.arr)):
            if self.arr[h] == [key]:
                self.arr[h].remove(key)
                y = h
                for y in range(i, (len(self.arr) - 1)):
                    if self.arr[h] != None:
                        self.arr[h] = self.arr[h + 1]
                        h += 1
                    if self.arr[h] == None:
                        self.arr[h - 1].clear
                        self.arr[h - 1].append(None)
                        break
                break
            elif self.arr[h] != [key]:
                h += 1
            else:
                print("Key not found")
    
    def setitem(self, key):
        h = self.get_hash(key)      
        for i in range(0, len(self.arr)):
            if self.arr[h] == [None]:
                self.arr[h].clear()
                self.arr[h].append(key)
                break
            elif self.arr[h] != [None]:
                h += 1
            elif self.arr[h] != [None] and self.arr[h] >= 11:
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
t.delitem(14)
print(t.arr)