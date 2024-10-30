# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        if not root:
            return res

        def dfs(cur, path):
            path.append(cur.val)
            if not cur.left and not cur.right:
                if sum(path) == targetSum:
                    res.append(path.copy())
                print(path)
                return
            if cur.left:
                dfs(cur.left, path)
                path.pop()

            

            if cur.right:
                dfs(cur.right, path)
                path.pop()

        
        dfs(root, [])

        return res        

        

        