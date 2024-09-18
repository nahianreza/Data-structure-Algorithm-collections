class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
     
        
        
        
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while r > l and bottom > top:   
            for toprow in range(l, r):   
                res.append(matrix[top][toprow])
            top += 1
            
            for rightcol in range(top, bottom):
                
                res.append(matrix[rightcol][r - 1])
            r -= 1

            if not (r > l and bottom > top):
                break
                
            for bottomrow in range(r - 1, l - 1 , -1):
               
                res.append(matrix[bottom -1][bottomrow])
            bottom -= 1
                
            for leftcol in range(bottom - 1, top - 1, -1):
            
                res.append(matrix[leftcol][l])

            l += 1

            
        
        return res
                
            
            
            
                
