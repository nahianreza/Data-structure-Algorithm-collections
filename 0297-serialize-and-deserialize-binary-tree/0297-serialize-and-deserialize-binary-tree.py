# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res  = []
        
        def dfs(cur):
            if not cur:
                res.append('N')
                return
            res.append(str(cur.val))
            
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)
        
        return ",".join(res)
        
        

    def deserialize(self, data):
        
        res = data.split(",")
        
        self.i = 0
        
        def dfs():
            if res[self.i] == 'N':
                self.i += 1
                return
            root = TreeNode(int(res[self.i]))
            self.i += 1
            
            root.left = dfs()
            root.right = dfs()
            
            return root 
        
        return dfs()
            
                
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))