# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findSubroot(root1,root2):
            if not root1:
                return False
            if dfs(root1, root2):
                return True
            return findSubroot(root1.left, root2) or findSubroot(root1.right, root2)
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val!= root2.val:
                return False
            
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        
        return findSubroot(root, subRoot)
        