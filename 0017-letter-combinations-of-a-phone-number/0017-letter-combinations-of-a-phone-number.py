class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        
        res = []
        
        word = {'2' : "abc",
                '3' : "def",
                '4' : "ghi",
                '5' : "jkl",
                '6' : "mno",
                '7' : "pqrs",
                '8' : "tuv",
                '9' : "wxyz"}
        
        def dfs(i, cur):
            if i >= len(digits):
                res.append(cur.copy())
                return

            for k in word[digits[i]]:
                cur.append(k)
                dfs(i+1, cur)
                cur.pop()
        dfs(0,[])

        res = ["".join(x) for x in res]
    
        return res
            


        
        
            
                
            
    
                        
            
                        
                        
        

            
            

        