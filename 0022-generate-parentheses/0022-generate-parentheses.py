# Stop when left count = right count = n
# left parentheses when left count < n
# right parentheses when right count < left count

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        res = []

        def dfs(leftCount, rightCount):
            if leftCount == rightCount == n:
                res.append("".join(stack))
                return
            if leftCount < n:
                stack.append('(')
                dfs(leftCount + 1, rightCount)
                stack.pop()
            if rightCount < leftCount:
                stack.append(')')
                dfs(leftCount, rightCount + 1)
                stack.pop()
        dfs(0,0)

        return res


        
            


            



        