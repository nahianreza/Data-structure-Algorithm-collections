class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        
        rowCol = set()
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rowCol.add((r,c))
                    
        for coordinates in rowCol:
            newRow = coordinates[0]
            newCol = coordinates[1]
            for i in range(row):
                matrix[i][newCol] = 0
            for j in range(col):
                matrix[newRow][j] = 0
                    
                    
    
                
                                   
                    
        