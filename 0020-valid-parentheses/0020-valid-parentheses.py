class Solution:
    def isValid(self, s: str) -> bool:
        hmap = { ')': '(', '}':'{', ']':'['}
        
        if len(s) == 1:
            return False

        stack = []

        for i in s:
            if i in hmap:
                if stack and hmap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        return True