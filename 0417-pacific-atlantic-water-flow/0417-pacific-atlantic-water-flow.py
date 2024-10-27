class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(i,j, prev, flowSet):
            if i < 0 or j < 0 or i == ROW or j == COL or (i,j) in flowSet or heights[i][j] < prev:
                return
            
            flowSet.add((i,j))
            
            directions = [(0,1), (0, -1), (1, 0), (-1,0)]

            for dx,dy in directions:
                dfs(i + dx, j + dy, heights[i][j], flowSet)

        for c in range(COL):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROW - 1, c, heights[ROW-1][c], atlantic)
        
        for r in range(ROW):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COL - 1, heights[r][COL-1], atlantic)

        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in pacific and (i, j) in atlantic:
                    res.append([i,j])

        return res

        

        
        