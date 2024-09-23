# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# we're gonna check if p < curr < q: curr
# if p and q < curr: curr -> curr.left
# if p and q > q : curr -> right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(curr, l, r):
            if (l.val < curr.val < r.val) or (r.val < curr.val < l.val) or (l.val == curr.val) or (r.val == curr.val):
                return curr
            elif l.val < curr.val and r.val < curr.val:
                return dfs(curr.left, l, r)
            elif l.val > curr.val and r.val > curr.val:
                return dfs(curr.right, l, r)
            
        
        return dfs(root,p,q)
                
                