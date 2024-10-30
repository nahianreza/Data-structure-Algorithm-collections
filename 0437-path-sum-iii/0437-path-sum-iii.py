# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        def dfs(cur, curSum):
            if not cur:
                return 
            curSum += cur.val

            if curSum == targetSum:
                self.res += 1
                
            dfs(cur.left, curSum)
            dfs(cur.right, curSum)
        

        def dfsRoot(cur):
            if not cur:
                return
            dfs(cur, 0)

            dfsRoot(cur.left)
            dfsRoot(cur.right)

        dfsRoot(root)

        return self.res
            

        