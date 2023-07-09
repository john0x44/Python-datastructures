def getHash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

class HashTable:
        def __init__(self):
            self.MAX = 100 
            self.arr = [[] for i in range(self.MAX)]

        def getHash(self, key):
            h = 0
            for char in key:
                h+=ord(char)
            return h % self.MAX

        def __setitem__(self, key, val):
            self.arr[self.getHash(key)] = val

        def __getitem__(self, key):
            return self.arr[self.getHash(key)]

        def __delitem__(self, key):
            hash = self.getHash(key)
            self.arr[hash] = None 
        # solve collisions using seperate chaining 
        # solve using linear probing

        
ht = HashTable()