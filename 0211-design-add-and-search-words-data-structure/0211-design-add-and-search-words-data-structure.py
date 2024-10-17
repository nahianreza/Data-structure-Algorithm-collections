class Trie:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
      
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = Trie()
            cur = cur.children[i]
        
        cur.EndOfWord = True

        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root

            for j in range(i, len(word)):
                c = word[j]

                if c == '.':
                    for node in cur.children.values():
                        if dfs(j + 1, node):
                            return True
                    return False
                
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.EndOfWord
        
        return dfs(0, self.root)


            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)