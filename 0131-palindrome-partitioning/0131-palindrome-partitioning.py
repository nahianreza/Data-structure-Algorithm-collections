class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []


        def isPalindrome(cur, l, r):

            while r > l:
                if cur[r] != cur[l]:
                    return False
                r -= 1
                l += 1
            return True

        def dfs(index):
            if index >= len(s):
                res.append(sol.copy())
                return
            
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    sol.append(s[index: i + 1])
                    dfs(i + 1)
                    sol.pop()
        
        dfs(0)
        return res


       

            
            