class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited = set()

        row, col = len(matrix), len(matrix[0])


        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0 and (r,c) not in visited:
                    for i in range(row):
                        if matrix[i][c] != 0:
                            matrix[i][c] = 0
                            visited.add((i,c))
                    for j in range(col):
                        if matrix[r][j] != 0:
                            matrix[r][j] = 0
                            visited.add((r, j))

        return matrix
    
        
    
                
                                   
                    
        