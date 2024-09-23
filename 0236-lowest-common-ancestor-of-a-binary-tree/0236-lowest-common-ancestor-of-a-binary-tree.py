# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #if node.left and node.right under node: then Lca is node
    # if node.right under node.left: then Lca is node.left
    #if node.left under node.right: then Lca is node.right
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p:
            return q
        if not q:
            return p
        if not p and not q:
            return None
        
        
        
        def dfs(curr):
            if curr == p or curr == q:
                return curr
            
            l = dfs(curr.left) if curr.left else None
            r = dfs(curr.right) if curr.right else None
            
            if l and r:
                return curr
            else:
                return l or r
                
                
        
        return dfs(root)
            