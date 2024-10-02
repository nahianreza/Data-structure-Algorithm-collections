class Node:
    def __init__(self):
        self.node = {}
        self.endOfWord = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
        
        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.node:
                cur.node[i] = Node()   
            cur = cur.node[i]
        
        cur.endOfWord = True
        
   
        

    def search(self, word: str) -> bool:
        
        cur = self.root
        
        for i in word:
            if i not in cur.node:
                return False
            cur = cur.node[i]
            
        
        return cur.endOfWord
   
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for i in prefix:
            if i not in cur.node:
                return False
            cur = cur.node[i]
        
        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)