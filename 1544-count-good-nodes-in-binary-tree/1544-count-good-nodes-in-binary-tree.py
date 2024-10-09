# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(cur, curMax):
            if not cur:
                return 
            
            if cur.val >= curMax:
                self.res += 1
                curMax = cur.val
            
            if cur.left:
                dfs(cur.left, curMax)
            if cur.right:    
                dfs(cur.right, curMax)
        
        dfs(root, root.val)

        return self.res
        