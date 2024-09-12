class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(1,0), (0, -1), (-1, 0), (0, 1)]
        res = 0
        visited = set()


        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == '0' or (x, y) in visited:
                return

            visited.add((x,y))

            for i in directions:
                dfs((x + i[0]),(y + i[1]))


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        
        return res

        
        


        