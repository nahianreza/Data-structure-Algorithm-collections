class Solution:
    def isValid(self, s: str) -> bool:
        hmap = { ')': '(', '}':'{', ']':'['}
        
        if len(s) == 1:
            return False
        
        stack = []
        
        for i in s:
            if i not in hmap:
                stack.append(i)
            else:
                if stack and stack[-1] == hmap[i]:
                    stack.pop()
                else:
                    return False
                    
                    
       
        if stack:
            return False
        return True