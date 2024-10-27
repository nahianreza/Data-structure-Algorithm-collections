class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()

        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i,j))
            area = 1


            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

            for x, y in directions:
                area += dfs(i + x, j + y)

            
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    newArea = dfs(i,j)
                    maxArea = max(newArea, maxArea)

        
        return maxArea
                    
        


                
        