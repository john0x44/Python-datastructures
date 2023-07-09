#Implement a trie data structure 


class TrieNode:
    def __init__(self):
        self.children = {} 
        self.isEnd=False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    
    # Insert word 
    def insert(self,word):
        cur = self.root
        for c in word: 
            if c not in cur.children:
                cur.children[c]=TrieNode() 
            cur = cur.children[c]
        cur.isEnd = True 
    
    # Search for word 
    def search(self,word):
        cur = self.root 
        for c in word: 
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return cur.isEnd 

    # Search for prefix 
    def searchPre(self,pre):
        cur = self.root 
        for c in pre: 
            if c not in cur.children:  
                return False 
            cur = cur.children[c]
        return True 

t = Trie() 
print(t.search("test"))
t.insert("test")
print(t.search("test"))
print(t.searchPre("tes"))