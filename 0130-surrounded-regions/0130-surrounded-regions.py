class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def dfs(i,j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or board[i][j] != 'O':
                return
            board[i][j] = 'T'

            directions = [(0,1), (0, -1), (1, 0), (-1,0)]

            for dx, dy in directions:
                dfs(dx + i, dy + j)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O' and (i in [0, ROW - 1] or j in [0, COL - 1]):
                    dfs(i,j)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

        


        