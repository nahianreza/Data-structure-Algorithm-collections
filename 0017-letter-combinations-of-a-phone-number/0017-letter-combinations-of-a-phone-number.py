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
        
        
        def dfs(digit, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            temp = digits[digit]
            for i in word[temp]:
                dfs(digit + 1, cur + i)
            
                
        dfs(0, "")
        
        return res
            
                
            
    
                        
            
                        
                        
        

            
            

        