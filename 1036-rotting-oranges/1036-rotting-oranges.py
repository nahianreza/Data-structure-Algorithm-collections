class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        ROW, COL = len(grid), len(grid[0])
        minute, fresh = 0, 0
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i,j])

        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for x, y in directions:
                    newRow, newCol = r + x, c + y

                    if newRow < 0 or newRow == ROW or newCol < 0 or newCol == COL or grid[newRow][newCol] != 1:
                        continue
                    grid[newRow][newCol] = 2
                    queue.append([newRow, newCol])
                    fresh -= 1
            
            minute += 1

        return minute if fresh == 0 else -1

                

        